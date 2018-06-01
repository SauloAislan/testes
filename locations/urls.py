#!/usr/bin/env python
#-*- coding: UTF-8 -*-

__author__ = "helljump"

from django.urls import path, include


from django.urls import path
from .views import map_view

urlpatterns = [
    path('', map_view, name='map_views'),
]