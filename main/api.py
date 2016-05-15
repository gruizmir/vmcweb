# -*- coding: utf-8 -*-
from django.http import Http404
from django.utils import timezone
from main.models import HackTeam, Pitch, Speaker, Sponsor, Workshop
from main.serializers import HackTeamSerializer, PitchSerializer, \
    SpeakerSerializer, SponsorSerializer, WorkshopSerializer
from rest_framework.response import Response
from rest_framework.views import APIView


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


class WorkshopList(APIView):
    u"""
    Lista de todos los speakers de la versión actual. Por ahora solo para
    obtener datos.
    """

    def get(self, request, format=None):
        year = request.GET.get('year', timezone.now().year)
        workshops = Workshop.objects.filter(version=year)
        serializer = WorkshopSerializer(workshops, many=True)
        return Response(serializer.data)