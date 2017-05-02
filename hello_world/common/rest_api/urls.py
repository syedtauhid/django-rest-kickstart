from django.conf.urls import url

from common.rest_api import views
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.utils.translation import ugettext_lazy as _

from rest_framework import status
from rest_framework.response import Response
import sys

urlpatterns = [
    url(r'^certificate/$', views.CertificateListAPIView.as_view()),
]
