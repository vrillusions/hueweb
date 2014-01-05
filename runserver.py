#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
"""Run flask app.

Starts the hueweb server using Flask's internal web server

"""

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

from hueweb import app


app.run(host=app.config['LISTEN_ADDRESS'])
