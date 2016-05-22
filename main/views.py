# -*- coding: utf-8 -*-
import random
import traceback
from django.conf import settings
from django.contrib.messages.views import SuccessMessageMixin
from django.core import mail
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.utils import timezone
from django.views.generic import FormView, View
from main.forms import ContactForm, HackTeamForm, PitchForm, \
                       SpeakerApplicationForm, SponsorForm
from main.models import Speaker, Sponsor
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


bgs = [
    '2015/bg/bg01.jpg',
    '2015/bg/bg02.jpg',
    '2015/bg/bg03.jpg',
    '2015/bg/bg04.jpg',
    '2015/bg/bg05.jpg',
    '2015/bg/bg06.jpg',
    '2015/bg/bg07.jpg',
    '2015/bg/bg08.jpg',
    '2015/bg/bg09.jpg',
    '2015/bg/bg10.jpg',
    '2015/bg/bg11.jpg',
    '2015/bg/bg12.jpg',
    '2015/bg/bg13.jpg'
]

available_years = [2015, 2016]


class HomeView(View):
    """
    Recibe el formulario de registro de un equipo para la hackathon.
    """
    success_url = '/'
    template_name = 'index.html'
    year = None

    def get_template(self):
        return str(self.year) + '/' + self.template_name

    def dispatch(self, request, year=2016):
        """
        Primera función llamada cuando se accede normalmente por navegador.
        """
        try:
            self.year = int(year)
        except:
            self.year = available_years[-1]

        return super(HomeView, self).dispatch(request=request)

    def get(self, request):
        # TODO: Documentar. Enviar a dispatch
        data = {'year': self.year}
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
        data['sponsors'] = Sponsor.objects.filter(version=self.year,
                                                  accepted=True)
        data['schedule'] = True
        speakers = Speaker.objects.filter(version=self.year)
        speakers_copy = speakers
        data['speakers'] = [speakers[i:i + 4]
                                        for i in range(0, speakers.count(), 4)]
        data['speakers_day_1'] = speakers_copy.filter(day=1)
        data['speakers_day_2'] = speakers_copy.filter(day=2)
        return render(request, self.get_template(), data)


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
    year = None

    def get_template(self):
        return str(self.year) + '/' + self.template_name

    def dispatch(self, request, year=2016):
        """
        Primera función llamada cuando se accede normalmente por navegador.
        """
        try:
            self.year = int(year)
        except:
            self.year = available_years[-1]
        return super(RegisterTeamView, self).dispatch(request=request)

    def get(self, request):
        data = {'year': self.year}
        data['bg'] = random.choice(bgs)
        data['title'] = u'Registro de equipos'
        return render(request, self.get_template(), data)

    def post(self, request):
        data = {'year': self.year}
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
            data['bg'] = random.choice(bgs)
            data['form'] = form
            data['title'] = u'Registro de equipos'
            return render(request, self.get_template(), data)


class SponsorView(SuccessMessageMixin, FormView):
    """
    Vista de registro de auspiciadores para el evento.
    """
    success_url = '/'
    template_name = 'new_sponsor.html'
    form_class = SponsorForm
    year = None

    def get_template(self):
        return str(self.year) + '/' + self.template_name

    def dispatch(self, request, year=2016):
        """
        Primera función llamada cuando se accede normalmente por navegador.
        """
        try:
            self.year = int(year)
        except:
            self.year = available_years[-1]
        return super(SponsorView, self).dispatch(request=request)

    def get(self, request):
        data = {'year': self.year}
        data['bg'] = random.choice(bgs)
        data['title'] = u'Auspicio'
        return render(request, self.get_template(), data)

    def post(self, request):
        data = {'year': self.year}
        data['bg'] = random.choice(bgs)
        data['title'] = u'Auspicio'
        form = SponsorForm(request.POST)
        if form.is_valid():
            sponsor = form.save()
            if not settings.DEBUG:
                self.send_email(sponsor)
            if request.is_ajax():
                return JsonResponse({'status': 'ok'}, status=200)
            else:
                self.request.session['sponsor_registered'] = True
                return HttpResponseRedirect(self.get_success_url())
        else:
            data['form'] = form
            if request.is_ajax():
                data = form.errors
                data['status'] = 'failure'
                return JsonResponse(data, status=400)
            else:
                return render(request, self.get_template(), data)

    def send_email(self, sponsor):
        """
        Función encargada de enviar un email de confirmación de recepción de
        email a la empresa interesada y un email a los organizadores.
        """
        subject = "[Valparaíso Mobile Conf] Solicitud de auspicio"
        msg = u'Estimado %(name)s, hemos recibido su solicitud de auspiciar ' +\
              u'el evento Valparaíso Mobile Conf. En breve, la organización ' +\
              u'del evento le contactará personalmente. \nMuchas gracias ' +\
              u'por apoyar esta gran iniciativa, Valparaíso Mobile Conf.' +\
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
    year = None

    def get_template(self):
        return str(self.year) + '/' + self.template_name

    def dispatch(self, request, year=2016):
        """
        Primera función llamada cuando se accede normalmente por navegador.
        """
        try:
            self.year = int(year)
        except:
            self.year = available_years[-1]
        return super(RegisterPitchView, self).dispatch(request=request)

    def get(self, request):
        data = {'year': self.year}
        data['bg'] = random.choice(bgs)
        data['title'] = u'Registro de pitch'
        data['form'] = self.form_class()
        return render(request, self.get_template(), data)

    def post(self, request):
        data = {'year': self.year}
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
            data['bg'] = random.choice(bgs)
            data['form'] = form
            data['title'] = u'Registro de pitch'
            return render(request, self.get_template(), data)


class MapView(View):
    """
    Recibe el formulario de registro de un equipo para la hackathon.
    """
    success_url = '/'
    template_name = 'map.html'
    year = None

    def get_template(self):
        return str(self.year) + '/' + self.template_name

    def dispatch(self, request, year=2016):
        """
        Primera función llamada cuando se accede normalmente por navegador.
        """
        try:
            self.year = int(year)
        except:
            self.year = available_years[-1]
        return super(MapView, self).dispatch(request=request)

    def get(self, request):
        # TODO: Documentar. Enviar a dispatch
        data = {'year': self.year}
        return render(request, self.get_template(), data)


# TODO: Ocupar Mixin de Javascript, Ajax o lo que haya
class SpeakerApplicationView(SuccessMessageMixin, FormView):
    """
    Vista de registro de auspiciadores para el evento.
    """
    form_class = SpeakerApplicationForm
    year = None

    def get_template(self):
        return str(self.year) + '/' + self.template_name

    def dispatch(self, request, year=2016):
        """
        Primera función llamada cuando se accede normalmente por navegador.
        """
        try:
            self.year = int(year)
        except:
            self.year = available_years[-1]
        return super(SpeakerApplicationView, self).dispatch(request=request)

    def post(self, request):
        data = {'year': self.year}
        form = SpeakerApplicationForm(request.POST)
        if form.is_valid():
            speaker_application = form.save(commit=False)
            speaker_application.year = self.year
            speaker_application.save()
            if not settings.DEBUG:
                self.send_email(speaker_application)
            return JsonResponse({'status': 'ok'}, status=200)
        else:
            data = form.errors
            data['status'] = 'failure'
            return JsonResponse(data, status=400)

    def send_email(self, speaker):
        """
        Función encargada de enviar un email de confirmación de recepción de
        email a la empresa interesada y un email a los organizadores.
        """
        subject = "[Valparaíso Mobile Conf] Postulación de charla"
        msg = u'Estimado %(name)s, hemos recibido su solicitud de exponer en' +\
              u'el evento Valparaíso Mobile Conf. En breve, la organización ' +\
              u'del evento le contactará personalmente. \nMuchas gracias ' +\
              u'por apoyar esta gran iniciativa, Valparaíso Mobile Conf.' +\
              u'\n\n Abdel Rojas Silva\nOrganizador'
        msg = msg % {'name': speaker.name}
        try:
            connection = mail.get_connection()
            connection.open()
            # TODO: Cambiar emails de organización por CC
            email = mail.EmailMessage(subject, msg, settings.DEFAULT_FROM_EMAIL,
                                      [speaker.email,
                                      'abdel.rojas@alumnos.usm.cl',
                                      'valpo.mobile.conf@gmail.com'],
                                      connection=connection)
            connection.send_messages([email])
            connection.close()
        except:
            print traceback.format_exc()


# TODO: Documentar
def initial_redirect(request):
    td = timezone.now()
    return HttpResponseRedirect(reverse('home', kwargs={'year': td.year}))

become_sponsor = SponsorView.as_view()
become_speaker = SpeakerApplicationView.as_view()
register_hack_team = RegisterTeamView.as_view()
pitch_view = RegisterPitchView.as_view()
home_view = HomeView.as_view()
map_view = MapView.as_view()
