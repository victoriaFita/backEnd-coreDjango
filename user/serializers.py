from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import User
from uploader.models import Image
from uploader.serializers import ImageSerializer

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['url', 'description', 'uploaded_on']


class UserSerializer(serializers.ModelSerializer):
    cover = ImageSerializer(read_only=True)

    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}


    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            cpf=validated_data.get('cpf', ''),
            telefone=validated_data.get('telefone', ''),
            data_nascimento=validated_data.get('data_nascimento', ''),
            cep=validated_data.get('cep', ''),
            is_staff=validated_data.get('is_staff', False),
            is_active=validated_data.get('is_active', True),
        )
        user.password = make_password(validated_data['password'])
        user.save()
        return user

