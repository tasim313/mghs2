SECRET_KEY = "django-insecure-m5i$q0t0qdw_n$xzmkt3+^7fe(=1xbnka)ey+e0i5^1b4*++-f"

DEBUG = True

ALLOWED_HOSTS = ['192.168.88.81', 'localhost', '127.0.0.1', '*']

INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    '192.168.88.81',
    # ...
]


ROOT_URLCONF = "Projectile.urls"

WSGI_APPLICATION = "Projectile.wsgi.application"

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


DJOSER = {
    'PASSWORD_RESET_CONFIRM_URL': 'users/password/reset/confirm/{uid}/{token}',
    # 'USERNAME_RESET_CONFIRM_URL': '#/username/reset/confirm/{uid}/{token}',
    'ACTIVATION_URL': 'users/activate/{uid}/{token}',
    'SEND_ACTIVATION_EMAIL': False,

    'LOGIN_FIELD': 'username',
    'USER_CREATE_PASSWORD_RETYPE': True,
    'SOCIAL_AUTH_ALLOWED_REDIRECT_URIS': ["http://127.0.0.1:8000/"],
}

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": ("rest_framework.authentication.TokenAuthentication",),
   
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
    
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser',
    ),
    "DEFAULT_PERMISSION_CLASSES": ["rest_framework.permissions.IsAuthenticated"],
}


EMAIL_HOST = ""
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = ""
EMAIL_HOST_PASSWORD = ""
DEFAULT_FROM_EMAIL = ""


SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
CSRF_COOKIE_PATH = '/'
CSRF_COOKIE_HTTPONLY = True
CSRF_TRUSTED_ORIGINS = ['http://192.168.88.81/']
DCS_SESSION_COOKIE_SAMESITE = "None"

AUTH_USER_MODEL = 'core.User'
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)
