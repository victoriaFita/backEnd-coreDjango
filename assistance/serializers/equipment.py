from rest_framework import serializers
from assistance.models import Equipment
from uploader.models import Image

class EquipmentSerializer(serializers.ModelSerializer):
    cover_attachment_key = serializers.UUIDField(write_only=True, required=False)

    class Meta:
        model = Equipment
        fields = "__all__"  # Make sure to include 'cover_attachment_key' if you're listing fields explicitly

    def create(self, validated_data):
        cover_attachment_key = validated_data.pop('cover_attachment_key', None)
        equipment = Equipment.objects.create(**validated_data)
        if cover_attachment_key:
            image = Image.objects.get(attachment_key=cover_attachment_key)
            equipment.cover = image
            equipment.save()
        return equipment

    def update(self, instance, validated_data):
        cover_attachment_key = validated_data.pop('cover_attachment_key', None)
        if cover_attachment_key:
            image = Image.objects.get(attachment_key=cover_attachment_key)
            instance.cover = image
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['cover'] = instance.cover.attachment_key if instance.cover else None
        return representation
