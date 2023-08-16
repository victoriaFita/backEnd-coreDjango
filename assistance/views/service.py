from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from assistance.models import Service
from assistance.serializers import ServiceSerializer

class ServiceViewSet(ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer