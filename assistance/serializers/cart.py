from rest_framework import serializers
from assistance.models import Cart, CartItem

class CartItemSerializer(serializers.ModelSerializer):
    item_name = serializers.CharField(source='item.name', read_only=True, required=False)
    equipment_name = serializers.CharField(source='equipment.name', read_only=True, required=False)

    class Meta:
        model = CartItem
        fields = ['id', 'cart', 'item', 'equipment', 'quantity', 'item_name', 'equipment_name']

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True, source='cartitem_set')

    class Meta:
        model = Cart
        fields = ['id', 'user', 'created_at', 'items']
