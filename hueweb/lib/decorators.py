# vim: set fileencoding=utf-8 :

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)
from functools import wraps

from flask import request, render_template, redirect, url_for

from hueweb import app


def templated(template=None):
    """Template decorator.

    Renders the given template file with values returned from view.

    """
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


def require_setup(func):
    """Require hue link to be setup before loading."""
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if 'api_user' not in app.config:
            return redirect(url_for('initial_setup'))
        return func(*args, **kwargs)
    return decorated_function
