#!/usr/bin/env python

# Copyright (C) 2012-2013 Lukas Lalinsky
# Distributed under the MIT license, see the LICENSE file for details.

import json
import logging
import time
from contextlib import closing
from acoustid.script import run_script
from acoustid.data.submission import import_queued_submissions
from acoustid.data.fingerprint import update_fingerprint_index

logger = logging.getLogger(__file__)


def do_import(script, index_first=False, only_index=False):
    with closing(script.engine.connect()) as db:
        if index_first:
            update_fingerprint_index(db, script.index)
        if not only_index:
            while True:
                count = import_queued_submissions(db, script.index, limit=10)
                if not count:
                    break
                update_fingerprint_index(db, script.index)


def main_master(script, opts, args):
    logger.info('Importer running in master mode')
    # first make sure the index is in sync with the database and
    # import already queued submissions
    do_import(script, index_first=True)
    # listen for new submissins and import them as they come
    channel = script.redis.pubsub()
    channel.subscribe('channel.submissions')
    for message in channel.listen():
        if message['type'] != 'message':
            continue
        try:
            ids = json.loads(message['data'])
        except Exception:
            logger.exception('Invalid notification message: %r', message)
            ids = []
        logger.debug('Got notified about %s new submissions', len(ids))
        do_import(script)
        logger.debug('Waiting for the next event...')


def main_slave(script, opts, args):
    logger.info('Importer running in slave mode, only updating the index')
    # import new fingerprints to the index every 15 seconds
    while True:
        started = time.time()
        do_import(script, index_first=True, only_index=True)
        delay = 15 - time.time() + started
        if delay > 0:
            logger.debug('Waiting %d seconds...', delay)
            time.sleep(delay)


def main(script, opts, args):
    if script.config.cluster.role == 'master':
        main_master(script, opts, args)
    else:
        main_slave(script, opts, args)


run_script(main)

