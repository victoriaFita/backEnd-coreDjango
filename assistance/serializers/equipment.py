from rest_framework import serializers
from assistance.models import Equipment
from uploader.models import Image

class CoverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['url', 'description', 'uploaded_on']

class EquipmentSerializer(serializers.ModelSerializer):
    cover = CoverSerializer(read_only=True)
    cover_attachment_key = serializers.UUIDField(write_only=True, required=False)

    class Meta:
        model = Equipment
        fields = '__all__'

    def create(self, validated_data):
        cover_attachment_key = validated_data.pop('cover_attachment_key', None)
        equipment = Equipment.objects.create(**validated_data)
        if cover_attachment_key:
            try:
                image = Image.objects.get(attachment_key=cover_attachment_key)
                equipment.cover = image
            except Image.DoesNotExist:
                raise serializers.ValidationError('Imagem não encontrada.')
        equipment.save()
        return equipment

    def update(self, instance, validated_data):
        cover_attachment_key = validated_data.pop('cover_attachment_key', None)
        if cover_attachment_key:
            image = Image.objects.get(attachment_key=cover_attachment_key)
            instance.cover = image
        instance.save()
        return super().update(instance, validated_data)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # Instead of just the attachment key, we now build a dictionary with more details
        if instance.cover:
            representation['cover'] = {
                'url': instance.cover.url,
                'description': instance.cover.description,
                'uploaded_on': instance.cover.uploaded_on.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
            }
        else:
            representation['cover'] = None
        return representation
