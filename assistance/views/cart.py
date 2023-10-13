from rest_framework import viewsets, status
from rest_framework.response import Response
from assistance.models import Cart, CartItem
from assistance.serializers import CartSerializer, CartItemSerializer

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        cart_items = CartItem.objects.filter(cart=instance)
        cart_item_serializer = CartItemSerializer(cart_items, many=True)
        return Response({
            'cart': serializer.data,
            'cart_items': cart_item_serializer.data
        })
