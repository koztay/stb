# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_auto_20161124_1824'),
    ]

    operations = [
        migrations.AddField(
            model_name='thumbnail',
            name='main_image',
            field=models.ForeignKey(default=1, to='products.ProductImage'),
            preserve_default=False,
        ),
    ]
