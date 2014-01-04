#!/usr/bin/env python
# vim:ts=4:sw=4:ft=python:fileencoding=utf-8
"""Python Template.

This is a template for python.
NOTE: The __future__ imports that make it more v3.x ready were added in v2.6.
Thus this template will only work in python v2.6 or higher.

For some info on documenting modules see:
http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

Requirements
    Python v2.6 or higher: This is due to the imports from future and to make
        this more compatible with version 3.x.

Environment Variables
    LOGLEVEL: overrides the level specified here. Choices are debug, info,
        warning, error, and critical. Default is warning.

"""

# Standard library imports
from __future__ import (division, absolute_import, print_function,
                        unicode_literals)


from flask import Flask


app = Flask(__name__)
from . import views