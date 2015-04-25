# -*- coding: utf-8 -*-
import random
import traceback
from django.conf import settings
from django.contrib.messages.views import SuccessMessageMixin
from django.core import mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import FormView, View
from main.models import Paper, Sponsor
from main.forms import RegisterForm, ContactForm, PaperForm, HackTeamForm, \
                       SponsorForm, AuthorForm
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

bgs = ['bg/bg01.jpg', 'bg/bg02.jpg', 'bg/bg03.jpg']


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
        if 'team' in request.GET and request.GET['team'] == '1':
            data['success_message'] = "Tu equipo ha sido registrado"
        elif 'u' in request.GET and request.GET['u'] == '1':
            data['success_message'] = "¡Gracias por inscribirte en " + \
                                      "Valparaíso Mobile Conf!"
        data['bg'] = random.choice(bgs)
        data['register_form'] = RegisterForm(prefix='register')
        data['contact_form'] = ContactForm(prefix='contact')
        data['sponsor_list'] = Sponsor.objects.all()
        papers = Paper.objects.filter(accepted=True)
        data['papers'] = papers
        data['schedule'] = True
        return render(request, self.template_name, data)


class RegisterUserView(FormView):
    """
    Recibe el formulario de registro de un asistente al evento.
    """
    success_url = '/?u=1'
    template_name = 'register.html'
    form_class = RegisterForm

    def dispatch(self, request):
        """
        Primera función llamada cuando se accede normalmente por navegador.
        """
        return super(RegisterUserView, self).dispatch(request=request)

    def get(self, request):
        data = {}
        data['bg'] = random.choice(bgs)
        return render(request, self.template_name, data)

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            subject = u'¡Gracias por inscribirte a Valparaíso Mobile Conf'
            msg = u'%(name)s, bienvenido a Valparaíso Mobile Conf. Estás ' + \
                  u'registrado para participar de las charlas del evento. ' + \
                  u'Si quieres participar de algún taller y aún no te ' +\
                  u'has registrado, revisa la sección talleres de nuestra web.'
            msg += u'\n\nTu código de registro es el %(code)s. '
            msg += u'\n\nEste código será solicitado si decides registrarte ' +\
                   u'para la hackathon o para otro taller. \n' +\
                   u'Unos días antes del evento, te enviaremos un ' +\
                   u'recordatorio y las instrucciones para identificarte en ' +\
                   u'la entrada del evento.'
            msg += u'\n\nAbdel Rojas Silva.\nOrganizador Valparaíso Mobile Conf.'
            msg = msg % {'name': user.name, 'code':user.reg_code}
            try:
                connection = mail.get_connection()
                connection.open()
                email = mail.EmailMessage(subject, msg,
                                          settings.DEFAULT_FROM_EMAIL,
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



#TODO: Enviar email a usuario y a valpo.mobile.conf@gmail.com
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
            return HttpResponseRedirect(self.get_success_url())
        else:
            data = {}
            data['bg'] = random.choice(bgs)
            data['form'] = form
            return render(request, self.template_name, data)


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
        data['paper_form'] = PaperForm(prefix='paper')
        data['author_form'] = AuthorForm(prefix='author')
        return render(request, self.template_name, data)

    def post(self, request):

        """
        Recibe los formularios para postulación de papers. Tiene dos formularios
        Django incrustados para recibir: uno es del paper propiamente tal, y el
        otro es de los archivos que se subirán con este.
        """
        form = PaperForm(request.POST, request.FILES, prefix='paper')
        author_form = AuthorForm(request.POST, prefix='author')
        data = {}
        data['bg'] = random.choice(bgs)
        if form.is_valid():
            if author_form.is_valid():
                author = author_form.save()
                paper = form.save()
                paper.authors.add(author)
                paper.save()
                self.sendEmail(paper)
                return HttpResponseRedirect(self.get_success_url())
            else:
                print author_form
                data['paper_form'] = form
                data['author_form'] = author_form
                return render(request, self.template_name, data)
        else:
            print form
            data['paper_form'] = form
            data['author_form'] = author_form
            return render(request, self.template_name, data)

    def sendEmail(self, paper):
        """
        Función encargada de enviar un email de confirmación de recepción de
        email al expositor.
        """
        subject = "[Valparaíso Mobile Conf] Recepción de paper"
        msg = u'Estimado %(name)s, su paper fue recibido exitosamente, y ' +\
              u'será evaluado por el jurado dentro del período de ' +\
              u'deliberación. Desde el %(fecha)s te avisaremos de los' +\
              u'resultados.\n\nMuchas gracias por participar de ' +\
              u'Valparaíso Mobile Conf. \n\n Abdel Rojas Silva\nOrganizador'
        msg = msg % {'name': paper.authors.all()[0].name,
                     'fecha': '08 de Junio de 2015'}
        try:
            connection = mail.get_connection()
            connection.open()
            email = mail.EmailMessage(subject, msg, settings.DEFAULT_FROM_EMAIL,
                                      [paper.authors.all()[0].email],
                                      connection=connection)
            connection.send_messages([email])
            connection.close()
        except:
            print traceback.format_exc()


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
        return render(request, self.template_name, data)

    def post(self, request):
        data = {}
        data['bg'] = random.choice(bgs)
        form = SponsorForm(request.POST)
        if form.is_valid():
            form.save()
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

become_sponsor = SponsorView.as_view()
register_hack_team = RegisterTeamView.as_view()
home_view = HomeView.as_view()
paper_view = RegisterPaperView.as_view()
register = RegisterUserView.as_view()