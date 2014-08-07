#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
from __future__ import absolute_import, print_function, unicode_literals

from flask.ext.script import Manager, Shell
from flask.ext.migrate import Migrate, MigrateCommand

from hueweb import app, db
from hueweb.models import *


manager = Manager(app)


migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


def make_shell_context():
    return dict(app=app, db=db)


manager.add_command('shell', Shell(make_context=make_shell_context))


if __name__ == "__main__":
    manager.run()
