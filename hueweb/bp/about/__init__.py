# vim: set fileencoding=utf-8 :
"""About section."""

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

from ...lib.decorators import templated
from ...metadata import __version__ as app_version


about = Blueprint('about', __name__, template_folder='templates')


# Need someway to pass the __version__ to this. May be easiest to just move that
# to it's own module so I can do a relative import then. at least neither of
# these worked:
#     from ... import __version__
#     from hueweb import __version__
@about.route('/')
@templated('about.html')
def show_about():
    values = {}
    values['version'] = app_version
    return values
#@about.route('/', defaults={'page': 'index'})
#@about.route('/<page>')
#def show(page):
#    try:
#        return render_template('pages/%s.html' % page)
#    except TempalateNotFound:
#        abort(404)
