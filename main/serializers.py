# -*- coding: utf-8 -*-
from rest_framework import serializers
from main.models import Speaker, Pitch, HackTeam, Sponsor, Workshop, Update


class SpeakerSerializer(serializers.ModelSerializer):
    """
    Clase que crea el string en formato JSON con los datos de un speaker
    """
    start_time = serializers.SerializerMethodField()

    class Meta:
        """
        Configuraciones para la creación del diccionario JSON, como el modelo
        que debe usar, los campos que envía y los campos de solo lectura.
        """
        model = Speaker
        exclude = ('email', 'phone', 'version', 'created')

    def get_start_time(self, obj):
        return obj.start_time.strftime("%H:%M")


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
        fields = ('id', 'name', 'lastname', 'email', 'app_name', 'updated')


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
                  'team_picture', 'project_description', 'updated')


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
        fields = ('name', 'url', 'logo', 'logo_thumb', 'updated')


class WorkshopSerializer(serializers.ModelSerializer):
    """
    Clase que crea el string en formato JSON con los datos de un taller.
    """
    start_time = serializers.SerializerMethodField()

    class Meta:
        """
        Configuraciones para la creación del diccionario JSON, como el modelo
        que debe usar, los campos que envía y los campos de solo lectura.
        """
        model = Workshop
        fields = ('id', 'title', 'teacher', 'day', 'start_time', 'description',
                  'twitter', 'linkedin', 'profile_picture', 'profile_thumbnail',
                  'image', 'updated')

    def get_start_time(self, obj):
        return obj.start_time.strftime("%H:%M")


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
