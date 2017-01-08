# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('importer', '0006_auto_20170108_2312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimportmap',
            name='type',
            field=models.CharField(blank=True, default='Generic Product', null=True, help_text='Product Type değeri yazılacak, Örneğin: "Generic Product"', max_length=120),
        ),
    ]
