# -*- coding: utf-8 -*-
from django import forms
from main.models import *


class AuthorForm(forms.ModelForm):

    class Meta:
        model = Person
        fields = ('name', 'lastname', 'phone', 'email')


class RegisterForm(forms.ModelForm):

    class Meta:
        model = Person
        exclude = ('reg_code', 'payed', 'photo_thumb', 'photo', 'creation_date')


class PaperForm(forms.ModelForm):

    class Meta:
        model = Paper
        exclude = ('accepted', 'authors', 'creation_date', 'start_time',
            'day_one')


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
