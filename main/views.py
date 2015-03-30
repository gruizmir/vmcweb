# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from main.models import Paper
from main.forms import RegisterForm, ContactForm
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


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
        register_form.save()
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_403_FORBIDDEN)


@api_view(["POST"])
def contact(request):
    contact_form = ContactForm(prefix='contact')
    if contact_form.is_valid():
        contact_form.save()
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_403_FORBIDDEN)