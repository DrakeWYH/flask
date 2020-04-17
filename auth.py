from functools import wraps
from flask import session, redirect, url_for


def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        user_id = session.get('user_id')
        if user_id:
            return func(*args, **kwargs)
        else:
            return redirect(url_for('login'))
    return wrapper
