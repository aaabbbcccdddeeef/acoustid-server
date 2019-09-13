# Copyright (C) 2014 Lukas Lalinsky
# Distributed under the MIT license, see the LICENSE file for details.

from acoustid.db import Session


class Database(object):

    def __init__(self):
        self.session_factory = Session
        self.session = None


db = Database()
