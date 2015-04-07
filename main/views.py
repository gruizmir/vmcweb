# -*- coding: utf-8 -*-
import random
from django.shortcuts import render_to_response
from django.template import RequestContext
from main.models import Paper
from main.forms import RegisterForm, ContactForm, PaperForm, PaperFilesForm, \
                       HackerForm
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


def home(request):
    bgs = ['bg01.jpg', 'bg02.jpg', 'bg03.jpg']
    data = {}
    data['bg'] = random.choice(bgs)
    data['register_form'] = RegisterForm(prefix='register')
    data['contact_form'] = ContactForm(prefix='contact')
    papers = Paper.objects.filter(accepted=True)
    data['papers'] = papers
    return render_to_response("index.html", data,
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


@api_view(["POST"])
def upload_paper(request):
    """
    Recibe los formularios para postulación de papers. Tiene dos formularios
    Django incrustados para recibir: uno es del paper propiamente tal, y el
    otro es de los archivos que se subirán con este.
    """
    paper_form = PaperForm(request.POST, prefix='paper')
    files_form = PaperFilesForm(request.POST, prefix='files')
    if paper_form.is_valid():
        if files_form.is_valid():
            paper = paper_form.save()
            files = files_form.save(commit=False)
            files.paper = paper
            files.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    else:
        return Response(status=status.HTTP_403_FORBIDDEN)


@api_view(["POST"])
def register_hack_team(request):
    """
    Recibe el formulario de registro de un equipo para la hackathon.
    """
    form = HackerForm(request.POST)
    if form.is_valid():
        form.save()
        return Response(status=status.HTTP_200_OK)

#TODO: url con name 'become_sponsor'
#TODO: nuevo formulario BecomeSponsor