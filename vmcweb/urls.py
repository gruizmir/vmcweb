from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'main.views.home_view', name='home'),
    url(r'^register/hackathon/', 'main.views.register_hack_team',
                                    name='register_hack_team'),
    url(r'^sponsor/', 'main.views.become_sponsor',
                                    name='become_sponsor'),
    url(r'^pitches/', 'main.views.pitch_view', name='new_pitch'),
    url(r'^contact/', 'main.views.contact', name='contact'),
    url(r'^admin/', include(admin.site.urls)),
)