# -*- coding: utf-8 -*-
from django import forms
from main.models import *


class RegisterForm(forms.ModelForm):

    class Meta:
        model = Person
        exclude = ('reg_code', 'payed', 'photo_thumb', 'photo', 'creation_date')


class PaperForm(forms.ModelForm):

    class Meta:
        model = Paper
        exclude = ('accepted', 'authors', 'creation_date')


class PaperFilesForm(forms.ModelForm):

    class Meta:
        model = PaperFile
        exclude = ('paper', 'upload_date')


class HackerForm(forms.ModelForm):

    class Meta:
        model = Hacker
        exclude = ('team',)


class ContactForm(forms.Form):
    name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=30)
    subject = forms.CharField(max_length=100)
    #TODO: Cambiar el widget
    message = forms.CharField(widget=forms.Textarea)
