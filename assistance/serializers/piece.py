from rest_framework.serializers import ModelSerializer

from assistance.models import Piece

class PieceSerializer(ModelSerializer):
    class Meta:
        model = Piece
        fields = "__all__"