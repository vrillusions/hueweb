# vim:ts=4:sw=4:ft=python:fileencoding=utf-8
"""Default configuration.

To make changes, copy this file to the project's instance folder and call it
config.py. Then adjust the settings as needed. Remove all the lines you didn't
change so not to confuse things on upgrade.

"""

from __future__ import absolute_import, print_function, unicode_literals


# Default configuration
# Flask specific
DEBUG = False
LOGGER_NAME = 'hueweb'

# What to listen on when running internal server
LISTEN_ADDRESS = '0.0.0.0'

# Database settings
SQLALCHEMY_DATABASE_URI = 'sqlite://'

# api credentials (not intended to be set in default config)
#api_user = 'SomeRandomWords'
#api_description = 'HueWeb'


