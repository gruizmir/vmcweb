# -*- coding: utf-8 -*-
from rest_framework import serializers
from main.models import Speaker, Pitch, HackTeam, Sponsor, Workshop, Update


class SpeakerSerializer(serializers.ModelSerializer):
    """
    Clase que crea el string en formato JSON con los datos de un speaker
    """
    class Meta:
        """
        Configuraciones para la creación del diccionario JSON, como el modelo
        que debe usar, los campos que envía y los campos de solo lectura.
        """
        model = Speaker
        exclude = ('email', 'phone', 'version', 'created', 'updated')


class PitchSerializer(serializers.ModelSerializer):
    """
    Clase que crea el string en formato JSON con los datos de un paper.
    Incluye los datos del autor(es).
    """
    class Meta:
        """
        Configuraciones para la creación del diccionario JSON, como el modelo
        que debe usar y los campos que envía.
        """
        model = Pitch
        fields = ('id', 'name', 'lastname', 'email', 'app_name')


class HackTeamSerializer(serializers.ModelSerializer):
    """
    Clase que crea el string en formato JSON con los datos de un taller.
    """

    class Meta:
        """
        Configuraciones para la creación del diccionario JSON, como el modelo
        que debe usar, los campos que envía y los campos de solo lectura.
        """
        model = HackTeam
        fields = ('id', 'name', 'leader', 'person2', 'person3', 'person4',
                  'team_picture', 'project_description')


class SponsorSerializer(serializers.ModelSerializer):
    """
    Clase que crea el string en formato JSON con los datos de un taller.
    """

    class Meta:
        """
        Configuraciones para la creación del diccionario JSON, como el modelo
        que debe usar, los campos que envía y los campos de solo lectura.
        """
        model = Sponsor
        fields = ('name', 'url', 'logo', 'logo_thumb')


class WorkshopSerializer(serializers.ModelSerializer):
    """
    Clase que crea el string en formato JSON con los datos de un taller.
    """

    class Meta:
        """
        Configuraciones para la creación del diccionario JSON, como el modelo
        que debe usar, los campos que envía y los campos de solo lectura.
        """
        model = Workshop
        fields = ('id', 'title', 'teacher', 'day', 'start_time', 'description',
                  'twitter', 'linkedin', 'profile_picture', 'image')


class UpdateSerializer(serializers.ModelSerializer):
    """
    Clase que crea el string en formato JSON con los datos de un taller.
    """

    class Meta:
        """
        Configuraciones para la creación del diccionario JSON, como el modelo
        que debe usar, los campos que envía y los campos de solo lectura.
        """
        model = Update
