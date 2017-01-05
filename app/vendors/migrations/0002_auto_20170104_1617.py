# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tedarikci',
            name='urunler',
            field=models.ManyToManyField(blank=True, to='products.Variation'),
        ),
    ]
