from rest_framework import serializers

from carts.models import Cart


class CartModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['user', 'items', 'total']

