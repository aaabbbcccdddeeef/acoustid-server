from sqlalchemy.orm import Session, sessionmaker
from acoustid.tables import metadata


class RoutingSession(Session):

    def __init__(self, *args, **kwargs):
        self._engines = kwargs.pop('engines', {})
        super(RoutingSession, self).__init__(*args, **kwargs)

    def get_bind(self, mapper=None, clause=None):
        return super(RoutingSession, self).get_bind(mapper, clause)


Session = sessionmaker(class_=RoutingSession)


def get_bind_args(engines):
    binds = {}
    for table in metadata.sorted_tables:
        bind_key = table.info.get('bind_key', 'main')
        if bind_key != 'main':
            binds[table] = engines[bind_key]
    return {'bind': engines['main'], 'binds': binds}


def get_session_args(script):
    kwargs = {
        'twophase': script.config.databases.use_two_phase_commit,
        'engines': script.db_engines,
    }
    kwargs.update(get_bind_args(script.db_engines))
    return kwargs


class DatabaseContext(object):

    def __init__(self, script):
        self.session = Session(**get_session_args(script))

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
