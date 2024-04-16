import re
import sys
from os.path import abspath, dirname, join
from pathlib import Path

from django.utils.translation import ugettext_lazy as _


def root(*dirs):
    base_dir = join(dirname(__file__), "..")
    return abspath(join(base_dir, *dirs))


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = dirname(dirname(abspath(__file__)))
APPS_DIR = root("apps")
sys.path.append(APPS_DIR)

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
APPS_DIR = root("apps")

STATICFILES_DIRS = (root("static"),)
STATIC_ROOT = root("collected_static")

FIXTURE_DIRS = (root("fixtures"),)

LOCALE_PATHS = (root("locale"),)

LOCAL_TMP_PATH = "/tmp/ubbc/"
Path(LOCAL_TMP_PATH).mkdir(parents=True, exist_ok=True)

ANONYMOUS_USER_NAME = None


# Application definition

DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

PACKAGED_APPS = [
    "django_countries",
    "multiselectfield",
    "phonenumber_field",
    "django.contrib.humanize",
    "rest_framework",
    "import_export",
]

PROJECT_APPS = [
    "core.apps.CoreConfig",
    "user.apps.UserConfig",
    "athlete.apps.AthleteConfig",
    "volunteer.apps.VolunteerConfig",
    "race.apps.RaceConfig",
    "event.apps.EventConfig",
]

INSTALLED_APPS = DJANGO_APPS + PACKAGED_APPS + PROJECT_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "ubbc.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "ubbc.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

ROOT_URLCONF = "ubbc.urls"

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "fr-FR"
LANGUAGES = (
    ("fr", _("french")),
    ("en", _("english")),
    ("es", _("spanish")),
)
LOCAL_LANGUAGES = {"fr": "fr-FR", "en": "en-US", "es": "es-ES"}

LANGUAGE_CODES = (
    ("fr-FR", _("french")),
    ("en-GB", _("english (UK)")),
    ("en-US", _("english (USA)")),
    ("es-ES", _("spanish")),
    ("pt-BR", _("brazilian portuguese")),
    ("zh-CN", _("chinese")),
    ("nl-NL", _("dutch")),
    ("fr-CA", _("canadian french")),
    ("fi-FI", _("finnish")),
    ("de-DE", _("german")),
    ("it-IT", _("italian")),
    ("ja-JP", _("japanese")),
    ("ko-KR", _("korean")),
    ("pl-PL", _("polish")),
    ("pt-PT", _("portuguese")),
    ("ru-RU", _("russian")),
    ("bg-BG", _("bulgarian")),
    ("hr-HR", _("croatian")),
    ("cs-CZ", _("czech")),
    ("da-DK", _("danish")),
    ("et-EE", _("estonian")),
    ("el-GR", _("greek")),
    ("hu-HU", _("hungarian")),
    ("lv-LV", _("latvian")),
    ("lt-LT", _("lithuanian")),
    ("mt-MT", _("maltese")),
    ("ro-RO", _("romanian")),
    ("sk-SK", _("slovak")),
    ("sl-SI", _("slovene")),
    ("sv-SE", _("swedish")),
    ("iw-IL", _("hebrew")),
    ("nb-NO", _("norwegian (bokmål)")),
    ("ar-SA", _("arabic saudi arabia")),
    ("ar-QA", _("arabic qatar")),
    ("ar-AE", _("arabic united arab emirates")),
    ("ar-DZ", _("arabic algeria")),
    ("ar-MA", _("arabic morocco")),
    ("ar-EG", _("arabic egypt")),
    ("ar-IL", _("arabic israel")),
    ("ar-JO", _("arabic jordan")),
    ("ar-KW", _("arabic kuwait")),
    ("ar-LB", _("arabic lebanon")),
    ("lo-LO", _("lorem ipsum")),
)

USE_I18N = True
USE_L10N = True

TIME_ZONE = "Europe/Paris"
USE_TZ = True

USE_THOUSAND_SEPARATOR = True
THOUSAND_SEPARATOR = " "
NUMBER_GROUPING = 3

IGNORABLE_404_URLS = (
    re.compile(r"\.(php|cgi)$"),
    re.compile(r"^/phpmyadmin/"),
    re.compile(r"^/apple-touch-icon.*\.png$"),
    re.compile(r"^/favicon\.ico$"),
    re.compile(r"^/robots\.txt$"),
)

DEBUG_TOOLBAR = False
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

AUTH_USER_MODEL = "user.User"

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SESSION_SAVE_EVERY_REQUEST = True
SESSION_COOKIE_AGE = 60 * 60 * 24 * 10
CSRF_COOKIE_SAMESITE = "Strict"  # as a string
SESSION_COOKIE_SAMESITE = "Strict"  # as a string
PHONENUMBER_DEFAULT_REGION = "FR"

DEFAULT_AUTO_FIELD = "core.fields.UUIDAutoField"
