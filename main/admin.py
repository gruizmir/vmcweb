# -*- coding: utf-8 -*-
from django.contrib import admin
from main.models import *


@admin.register(HackTeam)
class Admin(admin.ModelAdmin):
    list_display = ('name', 'email', 'creation_date')


@admin.register(Sponsor)
class SponsorAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_name', 'email', 'creation_date')


@admin.register(Pitch)
class PitchAdmin(admin.ModelAdmin):
    list_display = ('name', 'lastname', 'email', 'creation_date')