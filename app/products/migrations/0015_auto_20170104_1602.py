# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_auto_20170104_1245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producttype',
            name='name',
            field=models.CharField(default='Generic Product', max_length=120),
        ),
        migrations.AlterField(
            model_name='variation',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='variation',
            name='buying_curreny',
            field=models.ForeignKey(blank=True, null=True, to='products.Currency'),
        ),
        migrations.AlterField(
            model_name='variation',
            name='buying_price',
            field=models.DecimalField(decimal_places=2, blank=True, null=True, max_digits=20),
        ),
        migrations.AlterField(
            model_name='variation',
            name='product',
            field=models.ForeignKey(blank=True, null=True, to='products.Product'),
        ),
    ]
