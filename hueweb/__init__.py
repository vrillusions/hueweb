# vim: set fileencoding=utf-8 :

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

from flask import Flask

from .metadata import __version__


app = Flask(__name__, instance_relative_config=True)
app.config.from_object('hueweb.default_config')
app.config.from_pyfile('config.py', silent=True)

from . import logconfig
from . import blueprints
from . import views
