# -*- coding: utf-8 -*-
from rest_framework import serializers
from main.models import *


class PersonSerializer(serializers.ModelSerializer):
    """
    Clase que crea el string en formato JSON con los datos de una persona
    asistente.
    """
    class Meta:
        """
        Configuraciones para la creación del diccionario JSON, como el modelo
        que debe usar, los campos que envía y los campos de solo lectura.
        """
        model = Person
        fields = ('id', 'name', 'last_name', 'email', 'twitter',
                  'institution', 'photo', 'photo_thumb')


class PaperSerializer(serializers.ModelSerializer):
    """
    Clase que crea el string en formato JSON con los datos de un paper.
    Incluye los datos del autor(es).
    """
    authors = PersonSerializer(source='authors')
    class Meta:
        """
        Configuraciones para la creación del diccionario JSON, como el modelo
        que debe usar y los campos que envía.
        """
        model = Paper
        fields = ('authors', 'title', 'abstract')


class WorkshopSerializer(serializers.ModelSerializer):
    """
    Clase que crea el string en formato JSON con los datos de un taller.
    """
    expositor = PersonSerializer(source='expositor')

    class Meta:
        """
        Configuraciones para la creación del diccionario JSON, como el modelo
        que debe usar, los campos que envía y los campos de solo lectura.
        """
        model = Workshop
        fields = ('name', 'description', 'timespan', 'expositor')
