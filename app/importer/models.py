from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import post_save

from products.models import AttributeType, ProductType

# Create your models here.
# buraya mapping ile ilgili bir model koyabilirim.
# sonuçta her firmanın kendine has bir importer 'ı olacak.


default_fields = ("Ürün Adı", "Ürün Tanımı", "Ürün Kategorisi", "Ürün Resmi")


# bu map 'e ait bir de file field olmalı aslında ki o file'a ilişkin map olsun bu.
# hatta webden çekiyorsak çektiğimiz url 'yi de filed olarak girmeliyiz.
class ProductImportMap(models.Model):
    name = models.CharField(max_length=120)
    type = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Fields(models.Model):
    map = models.ForeignKey(ProductImportMap, blank=True, null=True)
    product_field = models.CharField(max_length=20, blank=True, null=True)  # bizdeki
    #  eşleşeceği field
    xml_field = models.CharField(max_length=1200, blank=True, null=True)  # XML  ya da excel deki field

    def __str__(self):
        return "%s - %s :" % (self.product_field, self.xml_field)


def import_map_post_save_receiver(sender, instance, *args, **kwargs):
    print("map_post_save_receiver çalıştı:", sender)  # sender ile instance farklı birbirinden
    print("instance:", instance)
    for field in default_fields:
        Fields.objects.get_or_create(map=instance, product_field=field)

    try:
        product_type = ProductType.objects.get(name=instance.type)
        product_features = AttributeType.objects.filter(product_type=product_type)
        for feature in product_features:
            Fields.objects.get_or_create(map=instance, product_field=feature.type)
    except:
        print("böyle bir product tipi yok")
        return False


post_save.connect(import_map_post_save_receiver, sender=ProductImportMap)
