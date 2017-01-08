# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_variation_buying_price_tl'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='default',
        ),
    ]
