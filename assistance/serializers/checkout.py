from rest_framework.serializers import ModelSerializer

from assistance.models import CheckOut

class CheckOutSerializer(ModelSerializer):
    class Meta:
        model = CheckOut
        fields = "__all__"