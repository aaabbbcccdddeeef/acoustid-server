# Copyright (C) 2011 Lukas Lalinsky
# Distributed under the MIT license, see the LICENSE file for details.

from nose.tools import *
from tests import (
    prepare_database, with_database,
    TEST_1_FP_RAW,
    TEST_1_LENGTH,
    TEST_1A_FP_RAW,
    TEST_1A_LENGTH,
    TEST_1B_FP_RAW,
    TEST_1B_LENGTH,
    TEST_1C_FP_RAW,
    TEST_1C_LENGTH,
    TEST_1D_FP_RAW,
    TEST_1D_LENGTH,
    TEST_2_FP_RAW,
    TEST_2_LENGTH,
)
from acoustid.data.track import (
    merge_missing_mbids, insert_track, merge_tracks,
    merge_mbids,
    calculate_fingerprint_similarity_matrix,
    can_merge_tracks,
    can_add_fp_to_track,
)


@with_database
def test_merge_mbids(conn):
    prepare_database(conn, """
TRUNCATE track_mbid CASCADE;
INSERT INTO track_mbid (track_id, mbid, submission_count) VALUES (1, '97edb73c-4dac-11e0-9096-0025225356f3', 9);
INSERT INTO track_mbid (track_id, mbid, submission_count) VALUES (1, 'd575d506-4da4-11e0-b951-0025225356f3', 11);
""")
    merge_mbids(conn, '97edb73c-4dac-11e0-9096-0025225356f3', ['d575d506-4da4-11e0-b951-0025225356f3'])
    rows = conn.execute("SELECT track_id, mbid, submission_count FROM track_mbid ORDER BY track_id, mbid").fetchall()
    expected_rows = [
        (1, '97edb73c-4dac-11e0-9096-0025225356f3', 20),
    ]
    assert_equals(expected_rows, rows)


@with_database
def test_merge_missing_mbids(conn):
    prepare_database(conn, """
TRUNCATE track_mbid CASCADE;
INSERT INTO track_mbid (track_id, mbid, submission_count) VALUES (1, '97edb73c-4dac-11e0-9096-0025225356f3', 1);
INSERT INTO track_mbid (track_id, mbid, submission_count) VALUES (1, 'b81f83ee-4da4-11e0-9ed8-0025225356f3', 1);
INSERT INTO track_mbid (track_id, mbid, submission_count) VALUES (1, 'd575d506-4da4-11e0-b951-0025225356f3', 1);
INSERT INTO track_mbid (track_id, mbid, submission_count) VALUES (2, 'd575d506-4da4-11e0-b951-0025225356f3', 1);
INSERT INTO track_mbid (track_id, mbid, submission_count) VALUES (3, '97edb73c-4dac-11e0-9096-0025225356f3', 1);
INSERT INTO track_mbid (track_id, mbid, submission_count) VALUES (4, '5d0290a6-4dad-11e0-a47a-0025225356f3', 1);
INSERT INTO musicbrainz.recording_gid_redirect (new_id, gid) VALUES
    (1, 'd575d506-4da4-11e0-b951-0025225356f3'),
    (2, '5d0290a6-4dad-11e0-a47a-0025225356f3'),
    (99, 'b44dfb2a-4dad-11e0-bae4-0025225356f3');
""")
    merge_missing_mbids(conn)
    rows = conn.execute("SELECT track_id, mbid FROM track_mbid ORDER BY track_id, mbid").fetchall()
    expected_rows = [
        (1, '97edb73c-4dac-11e0-9096-0025225356f3'),
        (1, 'b81f83ee-4da4-11e0-9ed8-0025225356f3'),
        (2, 'b81f83ee-4da4-11e0-9ed8-0025225356f3'),
        (3, '97edb73c-4dac-11e0-9096-0025225356f3'),
        (4, '6d885000-4dad-11e0-98ed-0025225356f3'),
    ]
    assert_equals(expected_rows, rows)


@with_database
def test_insert_track(conn):
    id = insert_track(conn)
    assert_equals(5, id)
    id = insert_track(conn)
    assert_equals(6, id)


@with_database
def test_merge_tracks(conn):
    prepare_database(conn, """
INSERT INTO fingerprint (fingerprint, length, track_id, submission_count)
    VALUES (%(fp1)s, %(len1)s, 1, 1), (%(fp2)s, %(len2)s, 2, 1);
INSERT INTO track_mbid (track_id, mbid, submission_count) VALUES (1, '97edb73c-4dac-11e0-9096-0025225356f3', 10);
INSERT INTO track_mbid (track_id, mbid, submission_count) VALUES (1, 'd575d506-4da4-11e0-b951-0025225356f3', 15);
INSERT INTO track_mbid (track_id, mbid, submission_count) VALUES (2, 'd575d506-4da4-11e0-b951-0025225356f3', 50);
INSERT INTO track_mbid (track_id, mbid, submission_count) VALUES (3, '97edb73c-4dac-11e0-9096-0025225356f3', 25);
INSERT INTO track_mbid (track_id, mbid, submission_count) VALUES (4, '5d0290a6-4dad-11e0-a47a-0025225356f3', 30);
INSERT INTO track_puid (track_id, puid, submission_count) VALUES (1, '97edb73c-4dac-11e0-9096-0025225356f4', 10);
INSERT INTO track_puid (track_id, puid, submission_count) VALUES (1, 'd575d506-4da4-11e0-b951-0025225356f4', 15);
INSERT INTO track_puid (track_id, puid, submission_count) VALUES (2, 'd575d506-4da4-11e0-b951-0025225356f4', 50);
INSERT INTO track_puid (track_id, puid, submission_count) VALUES (3, '97edb73c-4dac-11e0-9096-0025225356f4', 25);
INSERT INTO track_puid (track_id, puid, submission_count) VALUES (4, '5d0290a6-4dad-11e0-a47a-0025225356f4', 30);
    """, dict(fp1=TEST_1A_FP_RAW, len1=TEST_1A_LENGTH,
              fp2=TEST_1B_FP_RAW, len2=TEST_1B_LENGTH))
    merge_tracks(conn, 3, [1, 2, 4])
    rows = conn.execute("SELECT id, track_id FROM fingerprint ORDER BY id").fetchall()
    assert_true([(1, 3), (2, 3)], rows)
    rows = conn.execute("SELECT track_id, mbid, submission_count FROM track_mbid ORDER BY track_id, mbid").fetchall()
    expected = [
        (3, '5d0290a6-4dad-11e0-a47a-0025225356f3', 30),
        (3, '97edb73c-4dac-11e0-9096-0025225356f3', 35),
        (3, 'b81f83ee-4da4-11e0-9ed8-0025225356f3', 0),
        (3, 'd575d506-4da4-11e0-b951-0025225356f3', 65)
    ]
    assert_true(expected, rows)
    rows = conn.execute("SELECT track_id, puid, submission_count FROM track_puid ORDER BY track_id, puid").fetchall()
    expected = [
        (3, '5d0290a6-4dad-11e0-a47a-0025225356f4', 30),
        (3, '97edb73c-4dac-11e0-9096-0025225356f4', 35),
        (3, 'b81f83ee-4da4-11e0-9ed8-0025225356f4', 0),
        (3, 'd575d506-4da4-11e0-b951-0025225356f4', 65)
    ]
    assert_true(expected, rows)
    rows = conn.execute("SELECT id FROM track ORDER BY id").fetchall()
    assert_true([(3,)], rows)


@with_database
def test_track_fingerprint_matrix(conn):
    prepare_database(conn, """
INSERT INTO fingerprint (fingerprint, length, track_id, submission_count)
    VALUES (%(fp1)s, %(len1)s, 1, 1), (%(fp2)s, %(len2)s, 1, 1),
           (%(fp3)s, %(len3)s, 1, 1);
    """, dict(fp1=TEST_1A_FP_RAW, len1=TEST_1A_LENGTH,
              fp2=TEST_1B_FP_RAW, len2=TEST_1B_LENGTH,
              fp3=TEST_1C_FP_RAW, len3=TEST_1C_LENGTH))
    matrix = calculate_fingerprint_similarity_matrix(conn, [1])
    assert_equal([1, 2, 3], matrix.keys())
    assert_almost_equal(0.973319, matrix[1][2])
    assert_almost_equal(0.94152, matrix[1][3])
    assert_almost_equal(0.973319, matrix[2][1])
    assert_almost_equal(0.938414, matrix[2][3])
    assert_almost_equal(0.94152, matrix[3][1])
    assert_almost_equal(0.938414, matrix[3][2])


@with_database
def test_can_merge_tracks(conn):
    prepare_database(conn, """
INSERT INTO fingerprint (fingerprint, length, track_id, submission_count)
    VALUES (%(fp1)s, %(len1)s, 1, 1), (%(fp2)s, %(len2)s, 2, 1),
           (%(fp3)s, %(len3)s, 3, 1);
    """, dict(fp1=TEST_1A_FP_RAW, len1=TEST_1A_LENGTH,
              fp2=TEST_1B_FP_RAW, len2=TEST_1B_LENGTH,
              fp3=TEST_2_FP_RAW, len3=TEST_2_LENGTH))
    groups = can_merge_tracks(conn, [1, 2, 3])
    assert_equal([set([1, 2])], groups)


@with_database
def test_can_add_fp_to_track(conn):
    prepare_database(conn, """
INSERT INTO fingerprint (fingerprint, length, track_id, submission_count)
    VALUES (%(fp1)s, %(len1)s, 1, 1);
    """, dict(fp1=TEST_1A_FP_RAW, len1=TEST_1A_LENGTH))
    res = can_add_fp_to_track(conn, 1, TEST_2_FP_RAW, TEST_2_LENGTH)
    assert_equal(False, res)
    res = can_add_fp_to_track(conn, 1, TEST_1B_FP_RAW, TEST_1B_LENGTH + 20)
    assert_equal(False, res)
    res = can_add_fp_to_track(conn, 1, TEST_1B_FP_RAW, TEST_1B_LENGTH)
    assert_equal(True, res)

