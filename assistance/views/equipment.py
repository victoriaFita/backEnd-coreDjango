from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from assistance.models import Equipment
from assistance.serializers import EquipmentSerializer

class EquipmentViewSet(ModelViewSet):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer