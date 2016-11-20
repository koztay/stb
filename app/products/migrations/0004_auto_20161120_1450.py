# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_currency'),
    ]

    operations = [
        migrations.AddField(
            model_name='variation',
            name='buying_curreny',
            field=models.ForeignKey(default=None, to='products.Currency'),
        ),
        migrations.AddField(
            model_name='variation',
            name='buying_price',
            field=models.FloatField(default=1.0),
        ),
    ]
