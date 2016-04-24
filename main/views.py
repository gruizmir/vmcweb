# -*- coding: utf-8 -*-
import random
import traceback
from django.conf import settings
from django.contrib.messages.views import SuccessMessageMixin
from django.core import mail
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from django.utils import timezone
from django.views.generic import FormView, View
from main.forms import ContactForm, HackTeamForm, PitchForm, SponsorForm
from main.models import HackTeam, Pitch, Speaker, Sponsor
from main.serializers import HackTeamSerializer, PitchSerializer, \
                             SpeakerSerializer, SponsorSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView


bgs = ['bg/bg01.jpg', 'bg/bg02.jpg', 'bg/bg03.jpg', 'bg/bg04.jpg',
       'bg/bg05.jpg', 'bg/bg06.jpg', 'bg/bg07.jpg', 'bg/bg08.jpg',
       'bg/bg09.jpg', 'bg/bg10.jpg', 'bg/bg11.jpg', 'bg/bg12.jpg',
       'bg/bg13.jpg'
      ]


class HomeView(View):
    """
    Recibe el formulario de registro de un equipo para la hackathon.
    """
    success_url = '/'
    template_name = 'index.html'

    def dispatch(self, request):
        """
        Primera función llamada cuando se accede normalmente por navegador.
        """
        return super(HomeView, self).dispatch(request=request)

    def get(self, request):
        data = {}
        if request.session.pop('team_registered', False):
            data['success_message'] = "Tu equipo ha sido registrado"
        elif request.session.pop('pitch_registered', False):
            data['success_message'] = \
                        "Te has registrado exitosamente para mostrar tu app!"
        elif request.session.pop('registered', False):
            data['success_message'] = "¡Gracias por inscribirte en " + \
                                      "Valparaíso Mobile Conf!"
        elif request.session.pop('paper_registered', False):
            data['success_message'] = "¡Gracias por postular!" + \
                                      "Avisaremos de los resultados a partir" +\
                                      "del 19 de junio"
        elif request.session.pop('sponsor_registered', False):
            data['success_message'] = "¡Gracias por apoyar a Valparaíso " + \
                                      "Mobile Conf. La organización ha sido " +\
                                      "notificada y se pondrá en contacto " +\
                                      "usted a la brevedad."

        data['bg'] = random.choice(bgs)
        data['bg_reg'] = random.choice(bgs)
        data['contact_form'] = ContactForm(prefix='contact')
        data['sponsors'] = Sponsor.objects.filter(version=2016)
        data['schedule'] = True
        speakers = Speaker.objects.filter(version=2016)
        speakers_copy = speakers
        data['speakers'] = [speakers[i:i + 4]
                                        for i in range(0, speakers.count(), 4)]
        data['speakers_day_1'] = speakers_copy.filter(day=1)
        data['speakers_day_2'] = speakers_copy.filter(day=2)
        return render(request, self.template_name, data)


@api_view(["POST"])
def contact(request):
    contact_form = ContactForm(prefix='contact')
    if contact_form.is_valid():
        contact_form.save()
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_403_FORBIDDEN)


class RegisterTeamView(FormView):
    """
    Recibe el formulario de registro de un equipo para la hackathon.
    """
    success_url = '/'
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
        data['title'] = u'Registro de equipos'
        return render(request, self.template_name, data)

    def post(self, request):
        form = HackTeamForm(request.POST)
        if form.is_valid():
            team = form.save()
            subject = "Registro de Equipo a Valparaíso Mobile Conf"
            msg = "%(name)s, bienvenido a Valparaíso Mobile Conf. Tu equipo " +\
                  "ha sido correctamente registrado a la Hackathon. Como " +\
                  "respaldo, te enviamos una lista con tu equipo:" +\
                  "%(leader)s \n" +\
                  "%(person2)s\n%(person3)\n%(person4)s\n%(person5)"

            try:
                connection = mail.get_connection()
                connection.open()
                email = mail.EmailMessage(subject, msg,
                                          settings.DEFAULT_FROM_EMAIL,
                                          [team.email], connection=connection)
                connection.send_messages([email])
                connection.close()
            except:
                print traceback.format_exc()
            self.request.session['team_registered'] = True
            return HttpResponseRedirect(self.get_success_url())
        else:
            data = {}
            data['bg'] = random.choice(bgs)
            data['form'] = form
            data['title'] = u'Registro de equipos'
            return render(request, self.template_name, data)


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
        data['bg'] = random.choice(bgs)
        data['title'] = u'Auspicio'
        return render(request, self.template_name, data)

    def post(self, request):
        data = {}
        data['bg'] = random.choice(bgs)
        data['title'] = u'Auspicio'
        form = SponsorForm(request.POST)
        if form.is_valid():
            form.save()
            self.request.session['sponsor_registered'] = True
            return HttpResponseRedirect(self.get_success_url())
        else:
            data['form'] = form
            return render(request, self.template_name, data)

    def sendEmail(self, sponsor):
        """
        Función encargada de enviar un email de confirmación de recepción de
        email a la empresa interesada y un email a los organizadores.
        """
        subject = "[Valparaíso Mobile Conf] Solicitud de auspicio"
        msg = u'Estimado %(name)s, hemos recibido su solicitud de auspiciar ' +\
              u'el evento Valparaíso Mobile Conf. En breve, la organización ' +\
              u'del evento le contactará personalmente. \nMuchas gracias ' +\
              u'por apoyar esta gran inciativa, Valparaíso Mobile Conf.' +\
              u'\n\n Abdel Rojas Silva\nOrganizador'
        msg = msg % {'name': sponsor.contact_name}
        try:
            connection = mail.get_connection()
            connection.open()
            email = mail.EmailMessage(subject, msg, settings.DEFAULT_FROM_EMAIL,
                                      [sponsor.email,
                                      'abdel.rojas@alumnos.usm.cl',
                                      'gabriel.ruiz.miranda@gmail.com',
                                      'pablo.inzunza@alumnos.usm.cl'],
                                      connection=connection)
            connection.send_messages([email])
            connection.close()
        except:
            print traceback.format_exc()


class RegisterPitchView(FormView):
    u"""Recibe el formulario de registro de un equipo para la hackathon."""
    success_url = '/'
    template_name = 'register_pitch.html'
    form_class = PitchForm

    def dispatch(self, request):
        """
        Primera función llamada cuando se accede normalmente por navegador.
        """
        return super(RegisterPitchView, self).dispatch(request=request)

    def get(self, request):
        data = {}
        data['bg'] = random.choice(bgs)
        data['title'] = u'Registro de pitch'
        data['form'] = self.form_class()
        return render(request, self.template_name, data)

    def post(self, request):
        form = PitchForm(request.POST, request.FILES)
        if form.is_valid():
            pitch = form.save()
            subject = "Registro de Pitch a Valparaíso Mobile Conf"
            msg = u"%(name)s, bienvenido a Valparaíso Mobile Conf. \n\n" +\
                  u"Nuestro equipo te contactará en breve para asignar un " +\
                  u"horario para el pitch. ¡Gracias por tu interés!"
            msg = msg % {'name': form.cleaned_data['name']}
            try:
                connection = mail.get_connection()
                connection.open()
                email = mail.EmailMessage(subject, msg,
                                          settings.DEFAULT_FROM_EMAIL,
                                          to=[pitch.email],
                                          bcc=[settings.DEFAULT_FROM_EMAIL],
                                          connection=connection)
                connection.send_messages([email])
                connection.close()
            except:
                print traceback.format_exc()
            self.request.session['pitch_registered'] = True
            return HttpResponseRedirect(self.get_success_url())
        else:
            data = {}
            data['bg'] = random.choice(bgs)
            data['form'] = form
            data['title'] = u'Registro de pitch'
            return render(request, self.template_name, data)


# TODO: Revisar uso de Mixins
# http://www.django-rest-framework.org/tutorial/3-class-based-views/
class SpeakerList(APIView):
    u"""
    Lista de todos los speakers de la versión actual. Por ahora solo para
    obtener datos.
    """

    def get(self, request, format=None):
        year = request.GET.get('year', timezone.now().year)
        speakers = Speaker.objects.filter(version=year)
        serializer = SpeakerSerializer(speakers, many=True)
        return Response(serializer.data)


class SpeakerDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Speaker.objects.get(pk=pk)
        except Speaker.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        speaker = self.get_object(pk)
        serializer = SpeakerSerializer(speaker)
        return Response(serializer.data)


class HackTeamList(APIView):
    u"""
    Lista de todos los equipos para la hackathon de la versión actual. Por
    ahora solo para obtener datos.
    """

    def get(self, request, format=None):
        year = request.GET.get('year', timezone.now().year)
        teams = HackTeam.objects.filter(version=year)
        serializer = HackTeamSerializer(teams, many=True)
        return Response(serializer.data)


class PitchList(APIView):
    u"""
    Lista de todos los speakers de la versión actual. Por ahora solo para
    obtener datos.
    """

    def get(self, request, format=None):
        year = request.GET.get('year', timezone.now().year)
        pitchs = Pitch.objects.filter(version=year)
        serializer = PitchSerializer(pitchs, many=True)
        return Response(serializer.data)


class SponsorList(APIView):
    u"""
    Lista de todos los speakers de la versión actual. Por ahora solo para
    obtener datos.
    """

    def get(self, request, format=None):
        year = request.GET.get('year', timezone.now().year)
        sponsors = Sponsor.objects.filter(version=year)
        serializer = SponsorSerializer(sponsors, many=True)
        return Response(serializer.data)


become_sponsor = SponsorView.as_view()
register_hack_team = RegisterTeamView.as_view()
pitch_view = RegisterPitchView.as_view()
home_view = HomeView.as_view()
