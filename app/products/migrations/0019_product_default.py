# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0018_auto_20170109_1501'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='default',
            field=models.ForeignKey(related_name='default_category', to='products.Category', blank=True, null=True),
        ),
    ]
