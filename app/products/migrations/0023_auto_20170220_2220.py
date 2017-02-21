# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0022_auto_20170219_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='kdv',
            field=models.FloatField(default=18.0),
        ),
    ]
