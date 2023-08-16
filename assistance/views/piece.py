from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from assistance.models import Piece
from assistance.serializers import PieceSerializer

class PieceViewSet(ModelViewSet):
    queryset = Piece.objects.all()
    serializer_class = PieceSerializer