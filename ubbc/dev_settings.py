from decouple import Csv, config

from .settings import *

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {"format": "%(asctime)s [%(levelname)s] %(name)s: %(message)s"},
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "standard",
            "filters": [],
        },
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
            "level": "INFO",
        },
        "ubbc": {
            "handlers": ["console"],
            "level": "INFO",
        },
    },
}


# Django Settings
DEBUG = config("DEBUG", cast=bool, default=True)

SECRET_KEY = config("SECRET_KEY", default="development")
ALLOWED_HOSTS = config("ALLOWED_HOSTS", cast=Csv(), default="127.0.0.1, localhost")

MEDIA_URL = "/media/"
MEDIA_ROOT = "media/"
STATIC_URL = "/static/"
STATICFILES_DIRS = (root("static"),)
STATIC_ROOT = "collectstatic"
UPLOAD_ROOT = MEDIA_ROOT
UPLOAD_DIR = "/uploads/"
METADATA_DIR = "/metadata/"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": config("DB_NAME", default="ubbcdev"),
        "USER": config("DB_USER", default="pgdbuser"),
        "PASSWORD": config("DB_PASSWORD", default="pgdevpwd"),
        "HOST": config("DB_HOST", default="localhost"),
        "PORT": config("DB_PORT", default="5432"),
    }
}


EMAIL_BACKEND = config(
    "EMAIL_BACKEND", default="django.core.mail.backends.console.EmailBackend"
)

if EMAIL_BACKEND == "django.core.mail.backends.smtp.EmailBackend":
    EMAIL_HOST = config("EMAIL_HOST")
    EMAIL_PORT = config("EMAIL_PORT")
    EMAIL_HOST_USER = config("EMAIL_HOST_USER")
    EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD")

EMAIL_SECURITY = "TLS"
EMAIL_USE_TLS = EMAIL_SECURITY == "TLS"
EMAIL_USE_SSL = EMAIL_SECURITY == "SSL"


INTERNAL_IPS = ("127.0.0.1",)

INSTALLED_APPS += ["django_extensions"]

DEBUG_TOOLBAR = config("DEBUG_TOOLBAR", cast=bool, default=DEBUG)
DEBUG_TOOLBAR_USER_DEBUG = DEBUG_TOOLBAR


def show_toolbar(request):
    return DEBUG_TOOLBAR


DEBUG_TOOLBAR_PANELS = [
    "debug_toolbar_user_switcher.panels.UserPanel",
    "debug_toolbar.panels.versions.VersionsPanel",
    "debug_toolbar.panels.timer.TimerPanel",
    "debug_toolbar.panels.settings.SettingsPanel",
    "debug_toolbar.panels.headers.HeadersPanel",
    "debug_toolbar.panels.request.RequestPanel",
    "debug_toolbar.panels.sql.SQLPanel",
    "debug_toolbar.panels.staticfiles.StaticFilesPanel",
    "debug_toolbar.panels.templates.TemplatesPanel",
    "debug_toolbar.panels.cache.CachePanel",
    "debug_toolbar.panels.signals.SignalsPanel",
    "debug_toolbar.panels.logging.LoggingPanel",
    "debug_toolbar.panels.redirects.RedirectsPanel",
]

DEBUG_TOOLBAR_CONFIG = {
    "INTERCEPT_REDIRECTS": False,
}

MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]

INSTALLED_APPS += [
    "debug_toolbar_user_switcher",
    "debug_toolbar",
]

SITE_ID = 3

CURRENT_DOMAIN = "localhost:8000"
CURRENT_PROTOCOL = "http://"

WORD_GENERATOR_URL = "https://www.mit.edu/~ecprice/wordlist.10000"

if config("FILTER_LOGS", False):
    LOGGING["handlers"]["console"]["filters"].append("dev_filter")
