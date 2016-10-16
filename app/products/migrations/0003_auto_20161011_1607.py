# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20161011_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attributetype',
            name='product_type',
            field=models.ForeignKey(to='products.ProductType', blank=True, null=True),
        ),
    ]
