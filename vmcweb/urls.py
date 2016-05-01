# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = patterns('',
    url(r'(?P<year>[0-9]+)/', include('main.urls')),
    url(r'^api/', include('main.api_urls')),
    url(r'^contact/', 'main.views.contact', name='contact'),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)