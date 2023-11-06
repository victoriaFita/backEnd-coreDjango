from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from uploader.serializers.image import ImageUploadSerializer, ImageSerializer

from assistance.models import Equipment
from uploader.models import Image


class EquipmentSerializer(ModelSerializer):
    image = ImageUploadSerializer(required=False, allow_null=True)

    class Meta:
        model = Equipment
        fields = "__all__"

    def create(self, validated_data):
        image_data = validated_data.pop('image', None)
        equipment = Equipment.objects.create(**validated_data)
        if image_data:
            image_serializer = ImageUploadSerializer(data=image_data)
            if image_serializer.is_valid(raise_exception=True):
                equipment.image = image_serializer.save()
        equipment.save()
        return equipment

    def update(self, instance, validated_data):
        image_data = validated_data.pop('image', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if image_data:
            image_serializer = ImageUploadSerializer(instance.image, data=image_data)
            if image_serializer.is_valid(raise_exception=True):
                image_serializer.save()
        instance.save()
        return instance
