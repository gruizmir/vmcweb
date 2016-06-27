# -*- coding: utf-8 -*-
from ckeditor.widgets import CKEditorWidget
from django import forms
from django.contrib import admin
from main.models import Sponsor, HackTeam, Pitch, Speaker, SpeakerApplication,\
                        Workshop, Update


class VMCAdmin(admin.ModelAdmin):
    actions = ('duplicate', )
    save_on_top = True

    def duplicate(self, request, queryset):
        for item in queryset:
            item_copy = item
            item_copy.id = None
            item_copy.save()

    duplicate.short_description = u'Duplicar selección'


@admin.register(Sponsor)
class SponsorAdmin(VMCAdmin):
    list_display = ('name', 'contact_name', 'email', 'accepted', 'version')
    list_filter = ('version', )


@admin.register(Pitch)
class PitchAdmin(VMCAdmin):
    list_display = ('name', 'lastname', 'email', 'version')
    list_filter = ('version', )


@admin.register(Speaker)
class SpeakerAdmin(VMCAdmin):
    list_display = ('name', 'lastname', 'email', 'version')
    list_filter = ('version', 'day')


@admin.register(SpeakerApplication)
class SpeakerApplicationAdmin(VMCAdmin):
    actions = ('duplicate', )
    list_display = ('name', 'email', 'accepted')


@admin.register(HackTeam)
class HackTeamAdmin(VMCAdmin):
    list_display = ('leader', 'name', 'email', 'version')
    list_filter = ('version', )


@admin.register(Workshop)
class WorkshopAdmin(VMCAdmin):
    list_display = ('title', 'teacher', 'day', 'version')
    list_filter = ('version', 'day')


class UpdateAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())


@admin.register(Update)
class UpdateAdmin(VMCAdmin):
    form = UpdateAdminForm
    list_display = ('title', 'active', 'version', 'creation_date')
    list_filter = ('version', )
