# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('orders', '0009_auto_20150903_2250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(
                choices=[('created', 'Created'), ('paid', 'Paid'), ('shipped', 'Shipped'), ('refunded', 'Refunded')],
                max_length=120, default='created'),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='type',
            field=models.CharField(choices=[('billing', 'Billing'), ('shipping', 'Shipping')], max_length=120),
        ),
    ]
