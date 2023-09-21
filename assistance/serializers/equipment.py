from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from uploader.serializers.image import ImageUploadSerializer, ImageSerializer

from assistance.models import Equipment
from uploader.models import Image  

class EquipmentSerializer(ModelSerializer):
    image = ImageSerializer(required=False) 

    class Meta:
        model = Equipment
        fields = "__all__"

    def create(self, validated_data):
        image_data = validated_data.pop('image', None)
        
        if image_data:
            image_serializer = ImageUploadSerializer(data=image_data)
            if image_serializer.is_valid(raise_exception=True):
                image = image_serializer.save()
                validated_data['image'] = image

        equipment = Equipment.objects.create(**validated_data)
        return equipment

    def update(self, instance, validated_data):
        image_data = validated_data.pop('image', None)
        if image_data:
            # Se o Equipment já possui uma imagem, atualize-a
            if instance.image:
                image_serializer = ImageUploadSerializer(instance.image, data=image_data, partial=True)
            # Senão, crie uma nova imagem
            else:
                image_serializer = ImageUploadSerializer(data=image_data)
            
            if image_serializer.is_valid(raise_exception=True):
                image = image_serializer.save()
                validated_data['image'] = image
        
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
