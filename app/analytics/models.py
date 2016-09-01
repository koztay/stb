from django.conf import settings
from django.db import models

# Create your models here.

from products.models import Product


class ProductViewManager(models.Manager):
    def add_count(self, user, product):
        obj, created = self.model.objects.get_or_create(user=user,
                                                        product=product)
        obj.count += 1
        obj.save()
        return obj


class ProductView(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)
    product = models.ForeignKey(Product)
    count = models.IntegerField(default=0)

    objects = ProductViewManager()

    def __str__(self):
        return str(self.product.title)

