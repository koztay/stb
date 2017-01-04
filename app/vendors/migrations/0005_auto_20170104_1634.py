# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0004_vendor_isim'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='isim',
            field=models.CharField(unique=True, max_length=120),
        ),
    ]
