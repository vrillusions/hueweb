# vim: set fileencoding=utf-8 :
from __future__ import absolute_import, print_function, unicode_literals
import os
import logging
from logging.handlers import TimedRotatingFileHandler

from . import app


#app.logger.debug('setup file logger')
logfile = os.path.join(app.instance_path, 'hueweb.log')
file_handler = TimedRotatingFileHandler(
    logfile, when='midnight', backupCount=5)
file_handler.setLevel(logging.WARNING)
file_handler.setFormatter(logging.Formatter(
    '%(asctime)s - %(name)s - [%(pathname)s:%(lineno)d] - '
    '%(levelname)s - %(message)s'))

app.logger.addHandler(file_handler)
