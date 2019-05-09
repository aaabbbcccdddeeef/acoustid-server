#!/usr/bin/env python

# Copyright (C) 2011 Lukas Lalinsky
# Distributed under the MIT license, see the LICENSE file for details.

from acoustid.data.track import merge_missing_mbids


def main(script, opts, args):
    conn = script.engine.connect()
    with conn.begin():
        merge_missing_mbids(conn)
