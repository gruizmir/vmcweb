# -*- coding: utf-8 -*-
from django import forms
from main.models import HackTeam, Sponsor, Pitch, SpeakerApplication


class HackTeamForm(forms.ModelForm):
    class Meta:
        model = HackTeam
        exclude = ('creation_date',)


class SponsorForm(forms.ModelForm):
    class Meta:
        model = Sponsor
        fields = ('name', 'contact_name', 'email', 'phone')


class ContactForm(forms.Form):
    name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=30)
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)


class PitchForm(forms.ModelForm):
    phone = forms.CharField(required=False)

    class Meta:
        model = Pitch
        exclude = ('creation_date', 'accepted')


class SpeakerApplicationForm(forms.ModelForm):

    class Meta:
        model = SpeakerApplication
        fields = ('name', 'email', 'phone')