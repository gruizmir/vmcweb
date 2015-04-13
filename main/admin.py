# -*- coding: utf-8 -*-
from django.contrib import admin
from main.models import *


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'email', 'payed', 'creation_date')


@admin.register(HackTeam)
class Admin(admin.ModelAdmin):
    list_display = ('name', 'email', 'creation_date')


@admin.register(Paper)
class PaperAdmin(admin.ModelAdmin):
    list_display = ('title', 'accepted', 'creation_date')