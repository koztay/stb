# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20161120_2341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variation',
            name='buying_curreny',
            field=models.ForeignKey(to='products.Currency'),
        ),
    ]
