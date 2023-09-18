from rest_framework.serializers import ModelSerializer

from assistance.models import Equipment
from uploader.serializers.image import ImageSerializer

class EquipmentSerializer(ModelSerializer):
    image = ImageSerializer() 

    class Meta:
        model = Equipment
        fields = "__all__"