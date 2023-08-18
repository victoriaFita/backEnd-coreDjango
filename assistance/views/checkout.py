from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from assistance.models import CheckOut
from assistance.serializers import CheckOutSerializer

class CheckOutViewSet(ModelViewSet):
    queryset = CheckOut.objects.all()
    serializer_class = CheckOutSerializer
    