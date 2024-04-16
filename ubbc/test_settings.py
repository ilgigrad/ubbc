# pylint: disable=wildcard-import, unused-wildcard-import
from .settings import *

# Google Settings

GS_BUCKET_NAME = "test"

# Django Settings

DEBUG = True

SECRET_KEY = "testing"
ALLOWED_HOSTS = ["127.0.0.1", "localhost"]

TIME_ZONE = "UTC"
USE_TZ = True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "ubbctest",
        "USER": "ubbctestuser",
        "PASSWORD": "ubbctestpassword",
        "HOST": "localhost",
    }
}

DEFAULT_FILE_STORAGE = "django.core.files.storage.FileSystemStorage"

FIXTURE_DIRS = (root("fixtures"),)

STATIC_URL = "/static/"
MEDIA_ROOT = "/tmp/ubbc-media"
UPLOAD_DIR = "/tmp/ubbc-media/uploads/"
METADATA_DIR = "/tmp/ubbc-media/metadata/"
TMP_UPLOAD_PATH = UPLOAD_DIR + "currently_uploading/"


class DisableMigrations:
    def __contains__(self, item):
        return True

    def __getitem__(self, item):
        return None


if "makemigrations" not in sys.argv[1:]:
    MIGRATION_MODULES = DisableMigrations()

SITE_ID = 2

CURRENT_DOMAIN = "localhost:8000"
CURRENT_PROTOCOL = "http://"
