#!/usr/bin/env python
#-*- coding: UTF-8 -*-

__author__ = 'helljump'



from django.conf.urls import *
from django.urls import path, re_path
from django.contrib import admin
from django.contrib.auth import login
from django.views.generic import TemplateView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.http import HttpResponse
from rest_framework import routers

from locations import views

@api_view(['GET'])
def test_view(request, format=None):
    content = {
        'status': 'welcome'
    }
    return Response(content)


def login_success(request, format=None):
    token, created = Token.objects.get_or_create(user=request.user)
    resp = HttpResponse("success")
    resp.set_cookie("token", token)
    return resp


def login_error(request, format=None):
    return HttpResponse(status=401)


urlpatterns = [


    path('admin/', admin.site.urls),
    re_path(r'^login-success/$', login_success),
    re_path(r'^login-error/$', login_error),
    re_path(r'^test-view/$', test_view),
    path('', include('locations.urls')),
    path('index/<lat>/<lng>', views.send),
    re_path(r'^api/locations/$', views.LocationList.as_view()),
]

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()
