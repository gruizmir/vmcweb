# -*- coding: utf-8 -*-
from django.contrib import admin
from main.models import Sponsor, HackTeam, Pitch, Speaker


@admin.register(Sponsor)
class SponsorAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_name', 'email', 'version')


@admin.register(Pitch)
class PitchAdmin(admin.ModelAdmin):
    list_display = ('name', 'lastname', 'email', 'version')


@admin.register(Speaker)
class SpeakerAdmin(admin.ModelAdmin):
    list_display = ('name', 'lastname', 'email', 'version')


@admin.register(HackTeam)
class HackTeamAdmin(admin.ModelAdmin):
    list_display = ('leader', 'name', 'email', 'version')
