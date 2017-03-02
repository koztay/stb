from rest_framework import serializers

from carts.models import Cart, CartItem


class CartItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = CartItem
        fields = ['cart_item', 'quantity']


class CartModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['pk', 'items']

