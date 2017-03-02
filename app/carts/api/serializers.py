from django.http import Http404
from django.http import JsonResponse
from rest_framework import serializers

from carts.models import Cart, CartItem


class CartItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = CartItem
        fields = ['cart_item', 'quantity']


class CartModelSerializer(serializers.ModelSerializer):
    items = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ['pk', 'items']

    def get_items(self, obj):
            cart = Cart.objects.get(id=obj.pk)
            cart_items = cart.cartitem_set.all()
            print(cart_items)
            cart_items_array = []
            for cart_item in cart_items:
                item_in_cart = {
                    'product_title': cart_item.item.product.title,
                    'sale_price': cart_item.item.sale_price,
                    'quantity': cart_item.quantity,
                    'sub_total': cart_item.quantity * cart_item.item.sale_price,
                    'image': cart_item.item.product.micro_thumb,
                }
                cart_items_array.append(item_in_cart)
            return cart_items_array
