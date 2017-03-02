from rest_framework import serializers

from products.models import Product, Variation, ProductImage


class ProductModelSerializer(serializers.ModelSerializer):
    # images = serializers.RelatedField(source='product', read_only=True)

    class Meta:
        model = Product
        fields = ['title', 'micro_thumb', 'medium_thumb', 'sd_thumb', 'price', 'kdv']


class VariationModelSerializer(serializers.ModelSerializer):
    product = ProductModelSerializer()

    class Meta:
        model = Variation
        fields = ['product', 'price', 'sale_price']

"""
class Album(models.Model):
    album_name = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)

class Track(models.Model):
    album = models.ForeignKey(Album, related_name='tracks', on_delete=models.CASCADE)
    order = models.IntegerField()
    title = models.CharField(max_length=100)
    duration = models.IntegerField()

    class Meta:
        unique_together = ('album', 'order')
        ordering = ['order']

    def __unicode__(self):
        return '%d: %s' % (self.order, self.title)


"""