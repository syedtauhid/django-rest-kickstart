from django.http import HttpResponse
from django.utils.translation import ugettext_lazy as _

from common.models import Certificate
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.utils.translation import ugettext_lazy as _

from rest_framework import status
from rest_framework.response import Response
import sys

from rest_framework import status
from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, ListCreateAPIView,
                                     RetrieveAPIView, RetrieveUpdateAPIView,
                                     RetrieveUpdateDestroyAPIView,
                                     UpdateAPIView)
from rest_framework.response import Response
from rest_framework.views import APIView

class CertificateListAPIView(RetrieveAPIView):
    """
    This API view will provide -
    * List of certificates
    """

    def get_queryset(self):
        """
        Call the certificate service to get all the active instances.
        Returns all the active certificate as a list.

        :return: Certificate model instance list
        """
        return Certificate.objects.all()

    def get(self, request, *args, **kwargs):
        """
        Returns all the active certificate as Response object.

        :return: Response object for rest framework
        """
        return HttpResponse(self.get_queryset())
