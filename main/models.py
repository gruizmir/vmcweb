# -*- coding: utf-8 -*-
from django.db import models


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

    def __unicode__(self):
        return ('%s %s') % (self.name, self.last_name)


class Paper(models.Model):
    authors = models.ManyToManyField(Person)
    title = models.CharField(max_length=30, null=True, blank=False,
                            verbose_name='Título')
    abstract = models.TextField(verbose_name='Resumen')
    accepted = models.BooleanField(verbose_name='Aceptado', default=False)
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
    timespan = models.CharField(verbose_name="Duración", max_length=10)
    expositor = models.ForeignKey(Person, related_name="Expositor")

    class Meta:
        verbose_name = "Taller"
        verbose_name_plural = "Talleres"