# -*- coding: utf-8 -*-
from django import forms
from main.models import *


class HackTeamForm(forms.ModelForm):
    class Meta:
        model = HackTeam
        exclude = ('creation_date',)


class SponsorForm(forms.ModelForm):
    class Meta:
        model = Sponsor
        exclude = ('creation_date', 'logo_thumb', 'logo')


class ContactForm(forms.Form):
    name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=30)
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)


class PitchForm(forms.ModelForm):
    class Meta:
        model = Pitch
        exclude = ('creation_date', 'accepted', 'logo')