# -*- coding: utf-8 -*-
import os
from django.db import models
from cStringIO import StringIO
from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
from django.db.models.signals import post_delete
from django.dispatch import receiver
from PIL import Image


class Person(models.Model):
    name = models.CharField(max_length=30, null=True, blank=False,
                    verbose_name='Nombre')
    lastname = models.CharField(max_length=30, null=True, blank=False,
                    verbose_name='Apellido')
    rut = models.CharField(max_length=30, null=True, blank=True,
                    verbose_name='RUT/Pasaporte')
    email = models.EmailField(max_length=40, null=False, blank=False,
                    verbose_name='Email', unique=True)
    phone = models.CharField(max_length=15, null=True, blank=True,
                    verbose_name='Fono')
    twitter = models.CharField(max_length=30, null=True, blank=True,
                    verbose_name='Twitter')
    institution = models.CharField(max_length=30, null=True, blank=True,
                    verbose_name='RUT/Pasaporte')
    expositor = models.BooleanField(default=False,
                    verbose_name="Expositor")
    workshop = models.BooleanField(default=False,
                    verbose_name="Asiste a taller")
    creation_date = models.DateTimeField(auto_now_add=True,
                    verbose_name="Fecha de registro")
    payed = models.BooleanField(default=False,
                    verbose_name="Pagado")
    reg_code = models.CharField(max_length=20,
                    verbose_name="Código de registro")
    photo = models.ImageField(upload_to="profile_pics",
                    verbose_name="Foto")
    photo_thumb = models.ImageField(upload_to="profile_pics",
                    verbose_name="Thumbnail")

    class Meta:
        verbose_name = "Persona"
        verbose_name_plural = "Personas"

    def get_full_name(self):
        return ('%s %s') % (self.name, self.last_name)

    def __unicode__(self):
        return ('%s %s') % (self.name, self.last_name)


class Paper(models.Model):
    authors = models.ManyToManyField(Person)
    title = models.CharField(max_length=30, null=True, blank=False,
                            verbose_name='Título')
    abstract = models.TextField(verbose_name='Resumen')
    accepted = models.BooleanField(verbose_name='Aceptado', default=False)
    day_one = models.BooleanField(verbose_name='¿Día 1?',
      help_text="Participa en el día 1. Si está desmarcado, participa en día 2",
      default=False)
    start_time = models.TimeField(verbose_name='Hora de inicio',
            help_text='Rellenar sólo si es aceptada', null=True, blank=True)

    creation_date = models.DateTimeField(auto_now_add=True,
                    verbose_name="Fecha de creación")

    class Meta:
        verbose_name = "Paper"
        verbose_name_plural = "Papers"


class PaperFile(models.Model):
    paper = models.ForeignKey(Paper)
    doc = models.FileField(null=False, verbose_name="Archivo", blank=False,
                            upload_to="papers")
    extras = models.FileField(null=True, verbose_name="Anexos", blank=True,
                            upload_to="extras")
    description = models.TextField(verbose_name='Descripción', null=True,
                                    blank=True)
    upload_date = models.DateTimeField(auto_now_add=True,
                    verbose_name="Fecha de registro")

    class Meta:
        verbose_name = "Archivo adjunto"
        verbose_name_plural = "Archivos adjuntos"

    def __unicode__(self):
        return self.paper.title


class HackTeam(models.Model):
    name = models.CharField(max_length=40, verbose_name="Equipos")
    creation_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Equipo"
        verbose_name_plural = "Equipos"


class Hacker(Person):
    has_team = models.BooleanField(default=True)
    team = models.ForeignKey(HackTeam, blank=True, null=True)

    class Meta:
        verbose_name = "Hacker"
        verbose_name_plural = "Hackers"


class Workshop(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nombre")
    description = models.TextField(verbose_name="Descripción")
    assistant = models.ManyToManyField(Person, related_name="assistant")
    start_time = models.TimeField(verbose_name='Hora de inicio',
            help_text='Rellenar sólo si es aceptada', null=True, blank=True)
    timespan = models.CharField(verbose_name="Duración", max_length=10)
    expositor = models.ForeignKey(Person, related_name="Expositor")

    class Meta:
        verbose_name = "Taller"
        verbose_name_plural = "Talleres"


class Sponsor(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nombre")
    description = models.TextField(verbose_name="Descripción")
    url = models.URLField(null=True, blank=True)
    contact_name = models.CharField(max_length=50, verbose_name="Contacto")
    email = models.EmailField(max_length=40, null=False, blank=False,
                    verbose_name='Email', unique=True)
    phone = models.CharField(max_length=15, null=True, blank=True,
                    verbose_name='Fono')
    logo = models.ImageField(upload_to="logos",
                    verbose_name="Logo")
    logo_thumb = models.ImageField(upload_to="logos",
                    verbose_name="Thumbnail")
    creation_date = models.DateTimeField(auto_now_add=True)

    def createThumbnails(self):
        """
        Crea un thumbnail del avatar del usuario, con el menor tamaño (entre
        ancho y alto), definido por MAX_THUMBNAIL_SIZE en settings. Luego,
        guarda este thumbnail en el objeto Profile, campo profile_thumbnail.
        """
        if not self.logo:
            return
        img = Image.open(StringIO(self.logo.read()))

        PIL_TYPE = img.format.lower()
        if PIL_TYPE == 'jpeg':
            FILE_EXTENSION = 'jpg'
        elif PIL_TYPE == 'png':
            FILE_EXTENSION = 'png'

        width, height = img.size
        if width >= height:
            thumbWidth = settings.MAX_THUMBNAIL_SIZE
            thumbHeight = settings.MAX_THUMBNAIL_SIZE * height / width
        else:
            thumbHeight = settings.MAX_THUMBNAIL_SIZE
            thumbWidth = settings.MAX_THUMBNAIL_SIZE * width / height
        img.thumbnail((thumbWidth, thumbHeight), Image.ANTIALIAS)

        # Save the thumbnail
        temp_handle = StringIO()
        img.save(temp_handle, PIL_TYPE)
        temp_handle.seek(0)
        suf = SimpleUploadedFile(os.path.split(self.logo.name)[-1],
                                 temp_handle.read(),
                                 content_type='image/%s' % (PIL_TYPE))
        self.logo_thumb.save('%s.%s' % (os.path.splitext(suf.name)[0],
                                 FILE_EXTENSION), suf, save=False)


@receiver(post_delete, sender=Sponsor)
def sponsor_post_delete_handler(sender, **kwargs):
    """
    Recibe una señal de eliminación de una instancia de Sponsor. Elimina
    del sistema de archivos la foto real y el thumbnail asociados al avatar de
    esta instancia.
    """
    try:
        sponsor = kwargs['instance']
        storage, path = sponsor.logo.storage, sponsor.logo.path
        storageThumb, pathThumb = sponsor.logo_thumb.storage,\
                                    sponsor.logo_thumb.path
        if not path.endswith("no_disponible.jpg"):
            storage.delete(path)
            storageThumb.delete(pathThumb)
    except:
        pass


@receiver(post_delete, sender=Person)
def person_post_delete_handler(sender, **kwargs):
    """
    Recibe una señal de eliminación de una instancia de Person. Elimina
    del sistema de archivos la foto real y el thumbnail asociados al avatar de
    esta instancia.
    """
    try:
        person = kwargs['instance']
        storage, path = person.photo.storage, person.photo.path
        storageThumb, pathThumb = person.photo_thumb.storage,\
                                    person.photo_thumb.path
        if not path.endswith("no_disponible.jpg"):
            storage.delete(path)
            storageThumb.delete(pathThumb)
    except:
        pass