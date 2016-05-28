# -*- coding: utf-8 -*-
from ckeditor.widgets import CKEditorWidget
from django import forms
from django.contrib import admin
from main.models import Sponsor, HackTeam, Pitch, Speaker, SpeakerApplication,\
                        Workshop, Update


@admin.register(Sponsor)
class SponsorAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_name', 'email', 'accepted', 'version')
    list_filters = ('version', 'day')
    save_on_top = True


@admin.register(Pitch)
class PitchAdmin(admin.ModelAdmin):
    list_display = ('name', 'lastname', 'email', 'version')
    list_filters = ('version', )
    save_on_top = True


@admin.register(Speaker)
class SpeakerAdmin(admin.ModelAdmin):
    list_display = ('name', 'lastname', 'email', 'version')
    list_filters = ('version', )
    save_on_top = True


@admin.register(SpeakerApplication)
class SpeakerApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'accepted')
    save_on_top = True


@admin.register(HackTeam)
class HackTeamAdmin(admin.ModelAdmin):
    list_display = ('leader', 'name', 'email', 'version')
    list_filters = ('version', )
    save_on_top = True


@admin.register(Workshop)
class WorkshopAdmin(admin.ModelAdmin):
    list_display = ('title', 'teacher', 'day', 'version')
    list_filters = ('version', )
    save_on_top = True


class UpdateAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())


@admin.register(Update)
class UpdateAdmin(admin.ModelAdmin):
    form = UpdateAdminForm
    list_display = ('title', 'active', 'version', 'creation_date')
    list_filters = ('version', )
    save_on_top = True
