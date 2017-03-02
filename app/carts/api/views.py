from django.http import Http404
from carts.models import Cart
from .serializers import CartModelSerializer, CartItemSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response


class CartItemsListView(generics.ListAPIView):
    serializer_class = CartModelSerializer

    def get_queryset(self):
        cart_id = self.request.session.get("cart_id")
        return Cart.objects.filter(id=cart_id)


class CartDetailView(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Cart.objects.get(pk=pk)
        except Cart.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        cart = self.get_object(pk)
        serializer = CartModelSerializer(cart)
        return Response(serializer.data)