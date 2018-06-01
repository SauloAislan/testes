from django.shortcuts import render

# !/usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = 'helljump'

from .models import Location
from .serializers import LocationSerializer
from rest_framework import generics
from django.shortcuts import render
from django.http import HttpResponse


class LocationList(generics.ListCreateAPIView):
    serializer_class = LocationSerializer

    def get_queryset(self):
        user = self.request.user
        return Location.objects.filter(user=user)


def map_view(request):
    # points = Location.objects.filter(user=request.user)
    points = Location.objects.all()[:200]
    return render(request, 'map.html', {'points': points})


def send(request, lat, lng):
    p = Location(user_id=1, lat=lat, lng=lng, alt='10', time='2018-05-30 21:38:12')
    p.save()
    dados_list = Location.objects.all()
    for dados in dados_list:
        print
        dados.lng
    return HttpResponse(dados.lng)

