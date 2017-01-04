# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_auto_20170104_1602'),
    ]

    operations = [
        migrations.AddField(
            model_name='variation',
            name='buying_price_tl',
            field=models.DecimalField(null=True, blank=True, decimal_places=2, max_digits=20),
        ),
    ]
