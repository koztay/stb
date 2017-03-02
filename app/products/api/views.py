from rest_framework import generics

from products.models import Product,  Variation, ProductImage
from .serializers import ProductModelSerializer, VariationModelSerializer


class ProductListAPIView(generics.ListAPIView):
    serializer_class = ProductModelSerializer

    def get_queryset(self):
        # cart_id = self.request.session.get("cart_id")
        return Product.objects.all()


class VariationListAPIView(generics.ListAPIView):
    serializer_class = VariationModelSerializer

    def get_queryset(self):
        # cart_id = self.request.session.get("cart_id")
        return Variation.objects.all()
