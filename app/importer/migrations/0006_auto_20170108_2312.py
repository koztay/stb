# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('importer', '0005_auto_20170105_2220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fields',
            name='xml_field',
            field=models.CharField(null=True, max_length=1200, blank=True),
        ),
    ]
