import os

from django.contrib.messages import constants as messages
from django.core.exceptions import ImproperlyConfigured
from unipath import Path

import yaml

with open("config.yml", 'r') as ymlfile:
    cfg = yaml.full_load(ymlfile)

PROJECT_DIR = Path(__file__).ancestor(3)

# CKEditor configurations
CKEDITOR_ALLOW_NONIMAGE_FILES = False

CKEDITOR_CONFIGS = {
    'default': {
        'removePlugins':'smiley',
        'extraPlugins': 'stylesheetparser',
        'width': 'auto',
        'contentsCss': 'html, iframe, body, img {max-width:100%;}',
    },
}

# For clean_pyc to work without complaining
BASE_DIR = PROJECT_DIR

DEBUG = False

ADMINS = cfg['base']['admins']
SERVER_EMAIL = ADMINS[0][1]

DEFAULT_FROM_EMAIL = "Happiness Packets <fedora.happinesspackets@gmail.com>"

EMAIL_SUBJECT_PREFIX = "[happinesspackets] "

DOGSLOW_TIMER = 15
DOGSLOW_LOG_TO_FILE = False
DOGSLOW_LOGGER = 'dogslow'

TIME_ZONE = 'Europe/Amsterdam'
LANGUAGE_CODE = 'en-GB'
USE_I18N = True
USE_L10N = True
USE_TZ = True
DATE_FORMAT = 'j F Y'

CRISPY_TEMPLATE_PACK = 'bootstrap3'

SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
CSRF_COOKIE_HTTPONLY = True
SESSION_COOKIE_NAME = "PHPSESSID"
CSRF_COOKIE_NAME = "JSESSIONID"

ADMIN_ENABLED = False
MAX_MESSAGES = 20

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'
MESSAGE_TAGS = {
    messages.ERROR: 'danger',
}

MEDIA_ROOT = PROJECT_DIR.child('media')
MEDIA_URL = '/media/'
STATIC_ROOT = PROJECT_DIR.child('static')
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    PROJECT_DIR.child('assets'),
)

# noinspection PyUnresolvedReferences
MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'happinesspackets.utils.middleware.SetRemoteAddrFromForwardedFor',
    'dogslow.WatchdogMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]

ROOT_URLCONF = 'happinesspackets.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'happinesspackets.wsgi.application'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            PROJECT_DIR.child('templates'),
        ],
        'OPTIONS': {
            'context_processors': [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
                "happinesspackets.messaging.context_processors.packets_sent_processor",
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
        },
    },
]

INSTALLED_APPS = [
    'django.contrib.auth',
    'mozilla_django_oidc',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django.contrib.admin',
    'django.contrib.humanize',

    'django_extensions',
    'crispy_forms',
    'haystack',
    'happinesspackets.messaging',
    'djcelery_email',
    'ckeditor',
]


EMAIL_BACKEND = 'djcelery_email.backends.CeleryEmailBackend'

AUTHENTICATION_BACKENDS = (
    'happinesspackets.messaging.auth.OIDC',
)

OIDC_RP_SIGN_ALGO = 'RS256'
OIDC_RP_IDP_SIGN_KEY = '-----BEGIN RSA PUBLIC KEY-----\nMIIBCgKCAQEAq/0/XjILQxF3OaQZtFE3wVJ5UUuxZbxiJ/z+Zai0EOHiaMMxVyoo\nibDRen615r525DQ8TmQyR0eMQEpQ6SUvaOunahpYohgAkbkYggUMQhcoCLme18ZJ\nBTNWTP8w4t7mcuZd1cy1KtHpEvH4gkrjp8N3vIv1lzFraSc+p2rHMbV+AX5CJQ1H\nohBdwaqyOBKp0nzY27gu2EH2vzCwXkO4zGtrHfjjGc0Ra4WG+xz1AWg833xcFj3p\nqM3vca09jDLBme+GT151LcCCXRNyOZPZ3ZX62NxkMyqvVJHC3Uu2Q1hSHO7f6AZk\nZXY88PXXEH52T2ZrWiISowjTcGUboP8goQIDAQAB\n-----END RSA PUBLIC KEY-----\n'
OIDC_RP_CLIENT_ID = os.environ.get('OIDC_RP_CLIENT_ID')
OIDC_RP_CLIENT_SECRET = os.environ.get('OIDC_RP_CLIENT_SECRET')

ADMIN_USERNAME = os.getenv('ADMIN_USERNAME')
ADMIN_PASSWORD = os.getenv('ADMIN_PASSWORD')

OIDC_OP_AUTHORIZATION_ENDPOINT = "https://iddev.fedorainfracloud.org/openidc/Authorization"
OIDC_OP_TOKEN_ENDPOINT = "https://iddev.fedorainfracloud.org/openidc/Token"
OIDC_OP_USER_ENDPOINT = "https://iddev.fedorainfracloud.org/openidc/UserInfo"
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
LOGIN_REDIRECT_URL_FAILURE = '/error'
LOGIN_URL = '/oidc/authenticate/'
OIDC_RP_SCOPES = 'openid profile email'
OIDC_OP_LOGOUT_URL_METHOD = 'happinesspackets.messaging.auth.provider_logout'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(asctime)s gunicorn[%(process)d]: %(levelname)s %(name)s: %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(name)s: %(message)s'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue'
        },
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console': {
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
        }
    },
    'loggers': {
        'requests.packages.urllib3.connectionpool': {
            'handlers': ['null'],
            'propagate': False,
        },
        'stripe': {
            'handlers': ['null'],
            'propagate': False,
        },
        '': {
            'handlers': ['console', 'mail_admins'],
            'level': 'DEBUG',
            'propagate': True,
        },
    }
}

REDIS_HOST = 'localhost'
REDIS_PORT = '6379'
CELERY_BROKER_URL = 'redis://' + REDIS_HOST + ':' + REDIS_PORT + '/0'
BROKER_TRANSPORT_OPTIONS = {'visibility_timeout': 3600}
CELERY_RESULT_BACKEND = 'redis://' + REDIS_HOST + ':' + REDIS_PORT + '/0'

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': os.path.join(os.path.dirname(__file__), 'whoosh_index'),
    },
}

HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'

def get_env_variable(var_name):
    """ Get the environment variable or return exception """
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = "Set the %s environment variable" % var_name
        raise ImproperlyConfigured(error_msg)