from rest_framework.serializers import ModelSerializer

from assistance.models import Assistance

class AssistanceSerializer(ModelSerializer):
    class Meta:
        model = Assistance
        fields = "__all__"