# vim: set fileencoding=utf-8 :
from __future__ import absolute_import, print_function, unicode_literals

from . import app
from .bp.about import about


app.register_blueprint(about, url_prefix='/about')
