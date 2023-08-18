from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from assistance.models import Assistance
from assistance.serializers import AssistanceSerializer

class AssistanceViewSet(ModelViewSet):
    queryset = Assistance.objects.all()
    serializer_class = AssistanceSerializer