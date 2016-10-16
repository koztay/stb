# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_merge'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='attribute_types',
        ),
        migrations.RemoveField(
            model_name='product',
            name='attribute_values',
        ),
        migrations.RemoveField(
            model_name='producttype',
            name='attribute_type',
        ),
        migrations.RemoveField(
            model_name='producttype',
            name='attribute_value',
        ),
        migrations.RemoveField(
            model_name='producttype',
            name='product',
        ),
        migrations.AddField(
            model_name='attributetype',
            name='product_type',
            field=models.ForeignKey(default=1, to='products.ProductType'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='attributevalue',
            name='product',
            field=models.ForeignKey(null=True, blank=True, to='products.Product'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_type',
            field=models.ForeignKey(null=True, blank=True, to='products.ProductType'),
        ),
        migrations.RemoveField(
            model_name='attributetype',
            name='product',
        ),
        migrations.AddField(
            model_name='attributetype',
            name='product',
            field=models.ManyToManyField(blank=True, to='products.Product'),
        ),
    ]
