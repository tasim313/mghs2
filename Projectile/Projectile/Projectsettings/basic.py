from django.utils.translation import gettext_lazy as _
from .database import BASE_DIR

import os

ROOT_PATH = os.path.dirname(__file__)

DJANGO_APPS = [
    'jazzmin',
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

PROJECT_APP = [
    'core',
    'career',
]


THIRD_PARTY_APP = [
    'rest_framework',
    'rest_framework.authtoken',
    'djoser',
    'drf_yasg',
    'versatileimagefield',
    'import_export',
    "corsheaders",
    "debug_toolbar",
    'rosetta',
]

HEALTH_CHECK_APPS = [
    "health_check",
    "health_check.db",
    "health_check.cache",
    "health_check.storage",
    "health_check.contrib.migrations",
]


INSTALLED_APPS = DJANGO_APPS+PROJECT_APP+THIRD_PARTY_APP+HEALTH_CHECK_APPS


LANGUAGES = (
    ('en', _('English')),
    ('fr', _('French')),
    ('es', _('Spanish')),
    ('bn', _('Bengali')),
)

TIME_ZONE = 'Asia/Dhaka'

USE_I18N = True

USE_TZ = True


STATIC_URL = "/static/"


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

STATICFILES_DIRS = [
    os.path.join(ROOT_PATH, 'static')
]
STATIC_ROOT = os.path.join(BASE_DIR, 'assets')


MEDIA_DIR = BASE_DIR / 'media'

MEDIA_ROOT = MEDIA_DIR
MEDIA_URL = 'http://127.0.0.1:8000/media/'
MEDIA_URL_2 = '/media/'

HEALTH_CHECK = {
    "DISK_USAGE_MAX": 90,  # percent
    "MEMORY_MIN": 100,  # in MB
}

LOCALE_PATHS = [
    BASE_DIR / 'locale/',
]


SITE_ID = 2


CORS_ALLOWED_ORIGINS = [
    "https://example.com",
    "https://sub.example.com",
    "http://localhost:3000",
    'http://localhost:3001',
    'http://127.0.0.1:3000',
    'http://192.168.88.81:3000',
    'http://192.168.88.81:3001',
]

# CORS_ALLOW_METHODS = (
#     "DELETE",
#     "GET",
#     "OPTIONS",
#     "PATCH",
#     "POST",
#     "PUT",
# )

# CORS_ALLOW_HEADERS = (
#     "accept",
#     "authorization",
#     "content-type",
#     "user-agent",
#     "x-csrftoken",
#     "x-requested-with",
# )
