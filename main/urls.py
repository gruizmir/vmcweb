# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url


urlpatterns = patterns('main.views',
    url(r'^$', 'home_view', name='home'),
    url(r'^register/hackathon/', 'register_hack_team',
                                    name='register_hack_team'),
    url(r'^sponsor/new/', 'become_sponsor', name='become_sponsor'),
    url(r'^speaker/new/', 'become_speaker', name='become_speaker'),
    url(r'^pitches/add/', 'pitch_view', name='new_pitch'),
    url(r'^alojamiento/', 'map_view', name='lodging'),
)