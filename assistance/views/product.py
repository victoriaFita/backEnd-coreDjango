from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from assistance.models import Product
from assistance.serializers import ProductSerializer

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer