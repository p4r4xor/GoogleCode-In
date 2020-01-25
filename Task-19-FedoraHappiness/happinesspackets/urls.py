from __future__ import unicode_literals

import django
from django.conf import settings
from django.urls import include, re_path, path
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic.base import RedirectView

urlpatterns = [
    re_path(r'^oidc/', include('mozilla_django_oidc.urls')),
    re_path(r'^', include('happinesspackets.messaging.urls')),
]

if settings.ADMIN_ENABLED or settings.DEBUG:
    urlpatterns += [
        re_path(r'^admin/login/', RedirectView.as_view(url=settings.LOGIN_URL, permanent=True, query_string=True), name='admin_login'),
        re_path(r'^admin/', admin.site.urls, name='admin')
    ]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls))
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)