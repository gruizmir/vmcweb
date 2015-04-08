from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'main.views.home', name='home'),
    url(r'^register/user/', 'main.views.register', name='register'),
    url(r'^register/hackathon/', 'main.views.register_hack_team',
                                    name='hack_register'),
    url(r'^sponsor/', 'main.views.become_sponsor',
                                    name='become_sponsor'),
    url(r'^contact/', 'main.views.contact', name='contact'),
    url(r'^admin/', include(admin.site.urls)),
)
