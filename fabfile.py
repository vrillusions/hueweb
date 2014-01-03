
# vim:ts=4:sw=4:ft=python:fileencoding=utf-8

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)
import os
import sys
from contextlib import contextmanager

from fabric.api import env, task, local, lcd
from fabric.utils import abort, puts
from fabric.colors import red, green, yellow


# wrap in another dirname() if using a fabfile module directory
BASE_DIR = os.path.dirname(__file__)


env.colorize_errors = True
env.use_ssh_config = True


def _is_virtualenv():
    """Check if we are currently in a python virtualenv.

    :return: True if we are, False if not

    """
    virtualenv = os.getenv('VIRTUAL_ENV')
    is_virtualenv = False
    if virtualenv != None:
        is_virtualenv = True
    return is_virtualenv


# Setup a couple context managers
@contextmanager
def local_basedir():
    """Run commands relative to base directory."""
    with lcd(BASE_DIR):
        yield


# Begin tasks
#@task
def start_dev(address='0.0.0.0:8080'):
    """Start a dev instance listening on 0.0.0.0:8080."""
    with local_basedir():
        local('python manage.py runserver {}'.format(address))


@task
def freeze(requirements='requirements'):
    """Save all current python modules into a requirements file.
    (default: requirements (the .txt is added automatically))

    """
    with local_basedir():
        local('pip freeze -l >{}.txt'.format(requirements))


@task
def install(requirements='requirements'):
    """Run pip install with the given requirements file without '.txt'.
    (default: requirements)

    """
    if not _is_virtualenv():
        abort(red('Currently not in a virtualenv, canceling'))
    with local_basedir():
        local('pip install -r {}.txt'.format(requirements))
