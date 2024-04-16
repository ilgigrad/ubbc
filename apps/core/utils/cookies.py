from datetime import timedelta

from django.conf import settings


def get_session_cookie_age():
    return timedelta(seconds=settings.SESSION_COOKIE_AGE)
