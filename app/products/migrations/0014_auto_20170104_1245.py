# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_thumbnail_main_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='variation',
            name='istebu_product_no',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='variation',
            name='product_barkod',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
