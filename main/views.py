# -*- coding: utf-8 -*-
import random
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.views.generic import FormView
from main.models import Paper, Sponsor
from main.forms import RegisterForm, ContactForm, PaperForm, PaperFilesForm, \
                       HackerForm, SponsorForm
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


def home(request):
    bgs = ['bg01.jpg', 'bg02.jpg', 'bg03.jpg']
    data = {}
    data['bg'] = random.choice(bgs)
    data['register_form'] = RegisterForm(prefix='register')
    data['contact_form'] = ContactForm(prefix='contact')
    data['sponsor_list'] = Sponsor.objects.all()
    papers = Paper.objects.filter(accepted=True)
    data['papers'] = papers
    data['schedule'] = True
    return render_to_response("index.html", data,
                                  context_instance=RequestContext(request))


#TODO: Enviar email a usuario
def register(request):
    register_form = RegisterForm(prefix='register')
    if register_form.is_valid():
        register_form.save()
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_403_FORBIDDEN)


#TODO: Enviar email a usuario y a valpo.mobile.conf@gmail.com
@api_view(["POST"])
def contact(request):
    contact_form = ContactForm(prefix='contact')
    if contact_form.is_valid():
        contact_form.save()
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_403_FORBIDDEN)


#TODO: Debe enviar email de confirmación al posible expositor.
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


#TODO: Enviar email a cada uno de los miembros del equipo.
class RegisterTeamView(FormView):
    """
    Recibe el formulario de registro de un equipo para la hackathon.
    """
    success_url = '/'
    template_name = 'register_team.html'
    form_class = HackerForm

    def dispatch(self, request, device=None):
        """
        Primera función llamada cuando se accede normalmente por navegador.
        """
        return super(SponsorView, self).dispatch(request=request,
                                                   device=device)

    def get(self, request):
        data = {}
        return render(request, self.template_name, data)

    def post(self, request):
        form = HackerForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return render(request, self.template_name, {'form': form})


#TODO: Email de confirmación y notificación a organización
class SponsorView(FormView):
    """
    Vista del panel principal. Los cuadros se cargan con JS después de la carga
    de la página principal.
    """
    success_url = '/'
    template_name = 'new_sponsor.html'
    form_class = SponsorForm

    def dispatch(self, request, device=None):
        """
        Primera función llamada cuando se accede normalmente por navegador.
        """
        return super(SponsorView, self).dispatch(request=request,
                                                   device=device)

    def get(self, request):
        data = {}
        return render(request, self.template_name, data)

    def post(self, request):
        form = SponsorForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return render(request, self.template_name, {'form': form})


become_sponsor = SponsorView.as_view()
register_hack_team = RegisterTeamView.as_view()

#TODO: Crear modelo y formulario para Sponsor.