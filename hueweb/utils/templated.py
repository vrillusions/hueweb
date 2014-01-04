# vim:ts=4:sw=4:ft=python:fileencoding=utf-8

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)
from functools import wraps

from flask import request, render_template


def templated(template=None):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            template_name = template
            if template_name is None:
                template_name = request.endpoint \
                    .replace('.', '/') + '.html'
            ctx = f(*args, **kwargs)
            if ctx is None:
                ctx = {}
            elif not isinstance(ctx, dict):
                return ctx
            return render_template(template_name, **ctx)
        return decorated_function
    return decorator
