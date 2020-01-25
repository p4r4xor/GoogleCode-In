# -*- coding: utf-8 -*-
# noinspection PyUnresolvedReferences
import json
import sys

from .base import *  # noqa

DEBUG = True
TEMPLATES[0]['OPTIONS']['debug'] = True
CRISPY_FAIL_SILENTLY = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': 'db',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'example',
        'ATOMIC_REQUESTS': True,
        'CONN_MAX_AGE': 300,
    }
}

#Configurations to send email on console
CELERY_EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

#Configurations to test sending emails using Gmail SMTP
# CELERY_EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
# EMAIL_BACKEND = 'djcelery_email.backends.CeleryEmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_HOST_USER = '<HOST@EMAIL.COM>'
# EMAIL_HOST_PASSWORD = '<HOST_EMAIL_PASSWORD>'
# EMAIL_USE_TLS = True
# EMAIL_PORT = 587


SECRET_KEY = 'only-for-testing'

INTERNAL_IPS = ('127.0.0.1',)

DEBUG_TOOLBAR_CONFIG = {
    "SHOW_TOOLBAR_CALLBACK" : lambda request: DEBUG,
}


SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False

ADMIN_ENABLED = True

MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'happinesspackets.utils.middleware.SetRemoteAddrFromForwardedFor',
    'dogslow.WatchdogMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]

TESTING = 'test' in sys.argv

if not TESTING:

    MIDDLEWARE += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
    INSTALLED_APPS += (
        'debug_toolbar',
    )

SELENIUM_SCREENSHOT_DIR = PROJECT_DIR.child('selenium-screenshots')


# Uses a separate Docker container to act as the Redis server
CELERY_BROKER_URL = 'redis://redis:6379/0'
CELERY_RESULT_BACKEND = 'redis://redis:6379/0'

# Loads OIDC Client ID and Secret from client_secrets.json

with open("client_secrets.json") as f:
    secrets = json.load(f)
    OIDC_RP_CLIENT_ID = secrets["client_id"]
    OIDC_RP_CLIENT_SECRET = secrets["client_secret"]

# Reading the fas-id and Password
with open("fas-admin-details.json") as f:
    secrets = json.load(f)
    ADMIN_USERNAME = secrets["ADMIN_USERNAME"]
    ADMIN_PASSWORD =  secrets["ADMIN_PASSWORD"]

