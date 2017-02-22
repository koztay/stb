# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0023_auto_20170220_2220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='productfeatured',
            name='image',
            field=models.ImageField(upload_to=products.models.image_upload_to_featured, max_length=2000),
        ),
        migrations.AlterField(
            model_name='thumbnail',
            name='media',
            field=models.ImageField(upload_to=products.models.thumbnail_location, height_field='height', width_field='width', blank=True, max_length=2000, null=True),
        ),
    ]
