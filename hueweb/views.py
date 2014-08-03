# vim: set fileencoding=utf-8 :
"""Views."""

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)
import os
import hashlib
import platform
from random import SystemRandom
from functools import wraps

from flask import send_from_directory, g, request, redirect, url_for

from . import app
from .metadata import __version__ as app_version
from .lib.decorators import templated, require_setup


@app.route('/')
@templated('main.html')
@require_setup
def index():
    return dict(message='Hello World!')

@app.route('/initial_setup', methods=['GET', 'POST'])
@templated('initial_setup.html')
def initial_setup():
    if request.method == 'POST':
        # User submitted form, register the given user
        # Then write the instance/config.py file
        api_user = request.form['api_user']
        api_description = request.form['api_description']
        return redirect(url_for('/'))
    values = {}
    values['api_user'] = hashlib.md5(str(SystemRandom().random())).hexdigest()
    values['api_description'] = 'HueWeb on {}'.format(platform.node())
    return values

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
            'favicon.ico', mimetype='image/x-icon')

#@app.route('/about')
#@templated('about.html')
#def about():
#    values = {}
#    values['version'] = app_version
#    return values

# DEBUGGING
# look in to using logging.debug() instead
# print url rules
#print(app.url_map)
