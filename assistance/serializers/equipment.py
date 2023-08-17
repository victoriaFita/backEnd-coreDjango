from rest_framework.serializers import ModelSerializer

from assistance.models import Equipment

class EquipmentSerializer(ModelSerializer):
    class Meta:
        model = Equipment
        fields = "__all__"