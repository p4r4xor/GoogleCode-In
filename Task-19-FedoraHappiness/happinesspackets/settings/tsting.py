# noinspection PyUnresolvedReferences

# This file is intentionally named tsting instead of testing, as otherwise it would be
# imported during test discovery by the test runner, thereby accidentally activating the
# dev settings.

from .dev import *  # noqa

PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.MD5PasswordHasher',
)

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

#Disables toolbar for tests
DEBUG_TOOLBAR_CONFIG = {
    "SHOW_TOOLBAR_CALLBACK" : lambda request: False,
}
