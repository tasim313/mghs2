from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

LOGGING = {
    'version': 1,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.db.backends': {
            'level': 'DEBUG',
        },
        'health-check': {
            'handlers': ['console'],
            'level': 'WARNING',
            'propagate': True,
        }
    },
    # 'root': {
    #     'handlers': ['console'],
    # }
}