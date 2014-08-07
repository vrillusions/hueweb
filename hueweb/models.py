# vim: set fileencoding=utf-8 :
from __future__ import absolute_import, print_function, unicode_literals

from flask.ext.sqlalchemy import SQLAlchemy

from . import app, db


__all__ = ['Config']
__all__ = [n.encode('ascii') for n in __all__]


# TODO:2014-08-05:teddy: the DDL lines below don't get picked by alembic. They
# do get picked up when doing a db.create_all() though so maybe that's the
# workaround

class Config(db.Model):
    option = db.Column(db.String(50), primary_key=True)
    value = db.Column(db.String(100), nullable=True)
    created_at = db.Column(
        db.DateTime, nullable=False,
        server_default=db.text('CURRENT_TIMESTAMP'))
    updated_at = db.Column(
        db.DateTime, nullable=False,
        server_default=db.text('CURRENT_TIMESTAMP'))

    def __init__(self, option, value=None, created_at=None, updated_at=None):
        self.option = option
        self.value = value
        self.created_at = created_at
        self.updated_at = updated_at

    def __repr__(self):
        return '<Config %r>' % self.option


config_updated_at = db.DDL('''\
CREATE TRIGGER config_updated_at AFTER UPDATE ON config
    FOR EACH ROW
    BEGIN
        UPDATE config SET updated_at = CURRENT_TIMESTAMP
        WHERE option = old.option;
    END;''')
db.event.listen(Config.__table__, 'after_create', config_updated_at)


###
# Pretty sure the config_updated_at_insert is not needed. config_updated_at is
#
#config_updated_at_insert = db.DDL('''\
#CREATE TRIGGER config_updated_at_insert AFTER INSERT ON config
#    FOR EACH ROW
#    BEGIN
#        UPDATE config SET updated_at = CURRENT_TIMESTAMP
#        WHERE option = new.option;
#    END;''')
#db.event.listen(Config.__table__, 'after_create', config_updated_at_insert)
