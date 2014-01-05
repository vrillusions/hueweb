# vim: set fileencoding=utf-8 :
"""Views."""

# Standard library imports
from __future__ import (division, absolute_import, print_function,
                        unicode_literals)
import os

from flask import send_from_directory

from . import app
from .utils.templated import templated


@app.route('/')
@templated('basic_message.html')
def index():
    return dict(message='Hello World!')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
            'favicon.ico', mimetype='image/x-icon')
