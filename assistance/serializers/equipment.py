from rest_framework.serializers import ModelSerializer

from assistance.models import Equipment
from uploader.serializers.image import ImageSerializer

class EquipmentSerializer(ModelSerializer):
    image = ImageSerializer(required=False) 

    class Meta:
        model = Equipment
        fields = "__all__"

    def update(self, instance, validated_data):
        # Atualizando campos normais
        instance.name = validated_data.get('name', instance.name)
        instance.model = validated_data.get('model', instance.model)
        # ... (atualize os outros campos conforme necessário)

        # Atualizando a imagem
        image_data = validated_data.pop('image', None)
        if image_data:
            image_serializer = ImageSerializer(instance.image, data=image_data, partial=True)
            if image_serializer.is_valid():
                image_serializer.save()
            else:
                raise serializers.ValidationError(image_serializer.errors)
        
        instance.save()
        return instance
