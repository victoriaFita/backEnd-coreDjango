from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from assistance.models import Item
from assistance.serializers import ItemSerializer

class ItemViewSet(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer