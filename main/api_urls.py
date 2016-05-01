# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from main.api import SpeakerList, SpeakerDetail, SponsorList, HackTeamList,\
                        PitchList

urlpatterns = patterns('main.api',
    url(r'^speakers/$', SpeakerList.as_view()),
    url(r'^speakers/(?P<pk>[0-9]+)/$', SpeakerDetail.as_view()),
    url(r'^sponsors/$', SponsorList.as_view()),
    url(r'^teams/$', HackTeamList.as_view()),
    url(r'^pitches/$', PitchList.as_view()),
    url(r'^workshops/$', SponsorList.as_view()),
)