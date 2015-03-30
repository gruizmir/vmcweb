# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.http import require_http_methods
from main.models import Paper
from main.forms import RegisterForm, ContactForm
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics, permissions, status

def home(request):
    data = {}
    data['register_form'] = RegisterForm(prefix='register')
    data['contact_form'] = ContactForm(prefix='contact')
    papers = Paper.objects.filter(accepted=True)
    data['papers'] = papers
    return render_to_response("index.html", {data},
                                  context_instance=RequestContext(request))


@api_view(["POST"])
def register(request):
    register_form = RegisterForm(prefix='register')
    if register_form.is_valid():
        return HttpResponse("OK")
    else:
        return HttpResponse("ERROR")