# -*- coding: utf-8 -*-
import os
from django.db import models
from cStringIO import StringIO
from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
from django.db.models.signals import post_delete
from django.dispatch import receiver
from PIL import Image


class SpeakerApplication(models.Model):
    name = models.CharField(max_length=50, null=True, blank=False,
                    verbose_name='Nombre')
    lastname = models.CharField(max_length=50, null=True, blank=False,
                    verbose_name='Apellido')
    occupation = models.CharField(max_length=200, null=True, blank=True,
                    verbose_name='Cargo/Trabajo')
    email = models.EmailField(max_length=100, null=True, blank=False,
                    verbose_name='Email')
    profile_picture = models.ImageField(upload_to="speakers",
                    verbose_name="Logo", null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True,
                    verbose_name='Fono')
    twitter = models.CharField(max_length=60, null=True, blank=True,
                    verbose_name='Twitter')
    linkedin = models.CharField(max_length=200, null=True, blank=True,
                    verbose_name='Linkedin')
    title = models.CharField(max_length=100, null=True, blank=False,
                    verbose_name='Título de la charla')
    description = models.TextField(verbose_name='Descripción', null=True,
                                                               blank=True)
    version = models.IntegerField(verbose_name=u"Versión (Año)", null=False,
                                                    blank=False, default=2016)
    accepted = models.BooleanField("Aprobado", default=False)
    created = models.DateTimeField(auto_now_add=True,
                                            verbose_name="Creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Actualización")

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u"Postulación de Speaker"
        verbose_name_plural = u"Postulaciones de Speakers"
        app_label = 'main'


class Speaker(models.Model):
    DAY_OPTIONS = ((1, '1'), (2, '2'))
    name = models.CharField(max_length=50, null=True, blank=False,
                    verbose_name='Nombre')
    lastname = models.CharField(max_length=50, null=True, blank=False,
                    verbose_name='Apellido')
    occupation = models.CharField(max_length=200, null=True, blank=True,
                    verbose_name='Cargo/Trabajo')
    email = models.EmailField(max_length=100, null=True, blank=True,
                    verbose_name='Email')
    profile_picture = models.ImageField(upload_to="speakers",
                    verbose_name="Logo", null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True,
                    verbose_name='Fono')
    twitter = models.CharField(max_length=60, null=True, blank=True,
                    verbose_name='Twitter')
    linkedin = models.CharField(max_length=200, null=True, blank=True,
                    verbose_name='Linkedin')
    title = models.CharField(max_length=100, null=True, blank=False,
                    verbose_name='Título de la charla')
    description = models.TextField(verbose_name='Descripción', null=True,
                                                               blank=True)
    day = models.IntegerField(verbose_name="Día", null=True, blank=True,
                                                choices=DAY_OPTIONS)
    start_time = models.TimeField(verbose_name='Inicio de charla', null=True,
                                                                    blank=True)
    version = models.IntegerField(verbose_name=u"Versión (Año)", null=False,
                                                    blank=False, default=2016)
    created = models.DateTimeField(auto_now_add=True,
                                            verbose_name="Creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Actualización")

    def __unicode__(self):
        return self.name + " " + self.lastname

    class Meta:
        verbose_name = "Speaker"
        verbose_name_plural = "Speakers"
        app_label = 'main'


class Workshop(models.Model):
    DAY_OPTIONS = ((1, '1'), (2, '2'))
    title = models.CharField(max_length=150, null=True, blank=False,
                    verbose_name='Título')
    teacher = models.CharField(max_length=100, null=True, blank=False,
                    verbose_name='Relator')
    profile_picture = models.ImageField(upload_to="speakers",
                    verbose_name="Foto relator", null=True, blank=True)
    image = models.ImageField(upload_to="workshops",
                    verbose_name="Imagen referencial", null=True, blank=True)
    twitter = models.CharField(max_length=60, null=True, blank=True,
                    verbose_name='Twitter')
    linkedin = models.CharField(max_length=200, null=True, blank=True,
                    verbose_name='Linkedin')
    description = models.TextField(verbose_name='Descripción', null=True,
                                                               blank=True)
    day = models.IntegerField(verbose_name="Día", null=True, blank=True,
                                                choices=DAY_OPTIONS)
    start_time = models.TimeField(verbose_name='Inicio de charla', null=True,
                                                                    blank=True)
    version = models.IntegerField(verbose_name=u"Versión (Año)", null=False,
                                                    blank=False, default=2016)
    created = models.DateTimeField(auto_now_add=True,
                                            verbose_name="Creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Actualización")

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = "Taller"
        verbose_name_plural = "Talleres"
        app_label = 'main'


class Pitch(models.Model):
    name = models.CharField(max_length=50, null=True, blank=False,
                    verbose_name='Nombre')
    lastname = models.CharField(max_length=50, null=True, blank=False,
                    verbose_name='Apellido')
    email = models.EmailField(max_length=100, null=False, blank=False,
                    verbose_name='Email', unique=True)
    phone = models.CharField(max_length=15, null=True, blank=True,
                    verbose_name='Fono')
    app_name = models.CharField(max_length=100, null=True, blank=False,
                    verbose_name='Nombre de la app')
    description = models.TextField(verbose_name='Description', null=True,
                                                               blank=True)
    accepted = models.BooleanField(verbose_name='Aceptado', default=False)
    version = models.IntegerField(verbose_name=u"Versión (Año)", null=False,
                                                    blank=False, default=2016)
    creation_date = models.DateTimeField(auto_now_add=True,
                    verbose_name="Fecha de registro")
    extras = models.FileField(null=True, verbose_name="Anexos", blank=True,
                            upload_to="pitches")

    def __unicode__(self):
        return self.name + " " + self.lastname

    class Meta:
        verbose_name = "Pitch"
        verbose_name_plural = "Pitches"
        app_label = 'main'


class HackTeam(models.Model):
    name = models.CharField(max_length=40, verbose_name="Team Name",
                                unique=True)
    email = models.EmailField(max_length=30, verbose_name="Email de contacto",
                default="", unique=True,
                help_text="Usaremos este email para comunicarnos con ustedes ")
    phone = models.CharField(max_length=30, verbose_name="Teléfono de contacto",
            default="",
            help_text="Usaremos este teléfono para comunicarnos con ustedes ")
    leader = models.CharField(verbose_name="Team leader", max_length=40,
                                null=False, default="")
    lider_code = models.CharField(verbose_name="Código registro", max_length=40,
                null=True, blank=True,
                help_text="¿Registrado a las charlas? Ingresa tu código.")
    person2 = models.CharField(verbose_name="Hacker", max_length=40, null=False,
                default="")
    person2_code = models.CharField(verbose_name="Código registro", null=True,
                max_length=40, blank=True,
                help_text="¿Registrado a las charlas? Ingresa tu código.")
    person3 = models.CharField(verbose_name="Hacker", max_length=40,
                default="",
                null=False)
    person3_code = models.CharField(verbose_name="Código registro", null=True,
                max_length=40, blank=True,
                help_text="¿Registrado a las charlas? Ingresa tu código.")
    person4 = models.CharField(verbose_name="Hacker", max_length=40, null=True,
                                blank=True)
    person4_code = models.CharField(verbose_name="Código registro", null=True,
                max_length=40, blank=True,
                help_text="¿Registrado a las charlas? Ingresa tu código.")
    version = models.IntegerField(verbose_name=u"Versión (Año)", null=False,
                                                    blank=False, default=2016)
    team_picture = models.ImageField(upload_to="hackathon",
                            verbose_name="Foto Equipo", null=True, blank=True)
    project_description = models.TextField(null=True, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "Equipo"
        verbose_name_plural = "Equipos"
        app_label = 'main'


class Sponsor(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nombre")
    description = models.TextField(verbose_name="Descripción", null=True,
                                                                blank=True)
    url = models.URLField(null=True, blank=True)
    contact_name = models.CharField(max_length=50, verbose_name="Contacto",
                                                    null=True, blank=False)
    email = models.EmailField(max_length=40, null=True, blank=False,
                                    verbose_name='Email')
    phone = models.CharField(max_length=15, null=True, blank=True,
                    verbose_name='Fono')
    logo = models.ImageField(upload_to="logos",
                    verbose_name="Logo", null=True, blank=True)
    logo_thumb = models.ImageField(upload_to="logos",
                    verbose_name="Thumbnail", null=True, blank=True)
    accepted = models.BooleanField("Aprobado", default=False)
    version = models.IntegerField(verbose_name=u"Versión (Año)", null=False,
                                                    blank=False, default=2016)
    creation_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Auspiciador"
        verbose_name_plural = "Auspiciadores"
        app_label = 'main'

    def __unicode__(self):
        return self.name

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


class Update(models.Model):
    title = models.CharField(max_length=150, verbose_name="Título")
    description = models.TextField(verbose_name="Descripción", null=True,
                                                                blank=True)
    image = models.ImageField(upload_to="updates",
                    verbose_name="Foto", null=True, blank=True)
    image_thumb = models.ImageField(upload_to="updates",
                    verbose_name="Thumbnail", null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    active = models.BooleanField(verbose_name="Activo", default=False)
    version = models.IntegerField(verbose_name=u"Versión (Año)", null=False,
                                                    blank=False, default=2016)
    creation_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Actualización"
        verbose_name_plural = "Actualizaciones"
        app_label = 'main'

    def __unicode__(self):
        return self.title


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
