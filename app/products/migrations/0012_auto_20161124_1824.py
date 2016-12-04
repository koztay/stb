# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_auto_20161121_0009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productfeatured',
            name='product',
            field=models.ForeignKey(to='products.ProductImage'),
        ),
    ]
