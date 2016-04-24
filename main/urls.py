# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from django.views.generic.base import TemplateView
from main.views import SpeakerList, SpeakerDetail, SponsorList, HackTeamList,\
                        PitchList

urlpatterns = patterns('main.views',
    url(r'^$', 'home_view', name='home'),
    url(r'^register/hackathon/', 'register_hack_team',
                                    name='register_hack_team'),
    url(r'^sponsor/new/', 'become_sponsor', name='become_sponsor'),
    url(r'^pitches/add/', 'pitch_view', name='new_pitch'),
    url(r'^contact/', 'contact', name='contact'),
    url(r'^alojamiento/', TemplateView.as_view(template_name="map.html"),
                          name='lodging'),
    url(r'^speakers/$', SpeakerList.as_view()),
    url(r'^speakers/(?P<pk>[0-9]+)/$', SpeakerDetail.as_view()),
    url(r'^sponsors/$', SponsorList.as_view()),
    url(r'^teams/$', HackTeamList.as_view()),
    url(r'^pitches/$', PitchList.as_view()),
)