from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from uploader.serializers.image import ImageUploadSerializer, ImageSerializer

from assistance.models import Equipment
from uploader.models import Image


class EquipmentSerializer(ModelSerializer):
    image = ImageSerializer(required=False, allow_null=True)

    class Meta:
        model = Equipment
        fields = "__all__"

    def create(self, validated_data):
        image_data = validated_data.pop('image', None)

        if image_data:
            image_instance = Image.objects.get(attachment_key=image_data)
            validated_data['image'] = image_instance

        equipment = Equipment.objects.create(**validated_data)
        return equipment

    def update(self, instance, validated_data):
        image_data = validated_data.pop('image', None)
        if image_data:
            try:
                image_instance = Image.objects.get(attachment_key=image_data)
                validated_data['image'] = image_instance
            except Image.DoesNotExist:
                raise serializers.ValidationError({"image": "Image with provided attachment_key does not exist."})

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

