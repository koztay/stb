from rest_framework import generics

from carts.models import Cart
from .serializers import CartModelSerializer


class CartItemsListView(generics.ListAPIView):
    serializer_class = CartModelSerializer

    def get_queryset(self):
        cart_id = self.request.session.get("cart_id")
        return Cart.objects.filter(id=cart_id)
