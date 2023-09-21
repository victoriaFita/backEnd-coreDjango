from rest_framework.serializers import ModelSerializer, SlugRelatedField

from .models import User
from uploader.serializers.image import ImageSerializer

class UserSerializer(ModelSerializer):
    image = ImageSerializer(required=False)
    
    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = super(UserSerializer, self).create(validated_data)
        if password is not None:
            instance.set_password(password)
            instance.save()
        return instance
