from rest_framework.serializers import ModelSerializer, SlugRelatedField

from .models import User
from uploader.serializers.image import ImageSerializer

class UserSerializer(ModelSerializer):
    image = ImageSerializer() 
    class Meta:
        model = User
        fields = "__all__"
