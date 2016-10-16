# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('importer', '0002_auto_20161016_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fields',
            name='product_field',
            field=models.CharField(blank=True, null=True, max_length=20),
        ),
    ]
