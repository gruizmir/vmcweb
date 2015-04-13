# -*- coding: utf-8 -*-
import random
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.views.generic import FormView
from main.models import Paper, Sponsor
from main.forms import RegisterForm, ContactForm, PaperForm, HackTeamForm, \
                       SponsorForm
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

bgs = ['bg/bg01.jpg', 'bg/bg02.jpg', 'bg/bg03.jpg']

def home(request):
    data = {}
    if 'team' in request.GET and request.GET['team'] == '1':
        data['success_message'] = "Tu equipo ha sido registrado"
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


#TODO: Enviar email a cada uno de los miembros del equipo.
class RegisterTeamView(FormView):
    """
    Recibe el formulario de registro de un equipo para la hackathon.
    """
    success_url = '/?team=1'
    template_name = 'register_team.html'
    form_class = HackTeamForm

    def dispatch(self, request):
        """
        Primera función llamada cuando se accede normalmente por navegador.
        """
        return super(RegisterTeamView, self).dispatch(request=request)

    def get(self, request):
        data = {}
        data['bg'] = random.choice(bgs)
        return render(request, self.template_name, data)

    def post(self, request):
        form = HackTeamForm(request.POST)
        if form.is_valid():
            team = form.save()
            subject = "Registro de Equipo a Valparaíso Mobile Conf"
            msg = "%(name)s, bienvenido a Valparaíso Mobile Conf. Tu equipo " +\
                  "ha sido correctamente registrado a la Hackathon. Como " +\
                  "respaldo, te enviamos una lista con tu equipo:" +
                  "%(leader)s \n" +\
                  "%(person2)s\n%(person3)\n%(person4)s\n%(person5)"

            try:
                connection = mail.get_connection()
                connection.open()
                email = mail.EmailMessage(subject, msg, settings.EMAIL_HOST_USER,
                                          [user.email], connection=connection)
                connection.send_messages([email])
                connection.close()
            except:
                print traceback.format_exc()
            return HttpResponseRedirect(self.get_success_url())
        else:
            data = {}
            data['bg'] = random.choice(bgs)
            data['form'] = form
            return render(request, self.template_name, data)


#TODO: Enviar email a cada uno de los miembros del equipo.
class RegisterPaperView(FormView):
    """
    Recibe el formulario de registro de un equipo para la hackathon.
    """
    success_url = '/?paper=1'
    template_name = 'register_paper.html'
    form_class = PaperForm

    def dispatch(self, request):
        """
        Primera función llamada cuando se accede normalmente por navegador.
        """
        return super(RegisterPaperView, self).dispatch(request=request)

    def get(self, request):
        data = {}
        data['bg'] = random.choice(bgs)
        return render(request, self.template_name, data)

    #TODO: Debe enviar email de confirmación al posible expositor.
    def post(self, request):

        """
        Recibe los formularios para postulación de papers. Tiene dos formularios
        Django incrustados para recibir: uno es del paper propiamente tal, y el
        otro es de los archivos que se subirán con este.
        """
        form = PaperForm(request.POST, prefix='paper')
        if form.is_valid():
            paper = form.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            data = {}
            data['bg'] = random.choice(bgs)
            data['form'] = form
            return render(request, self.template_name, data)


#TODO: Email de confirmación y notificación a organización
class SponsorView(SuccessMessageMixin, FormView):
    """
    Vista de registro de auspiciadores para el evento.
    """
    success_url = '/'
    template_name = 'new_sponsor.html'
    form_class = SponsorForm

    def dispatch(self, request):
        """
        Primera función llamada cuando se accede normalmente por navegador.
        """
        return super(SponsorView, self).dispatch(request=request)

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