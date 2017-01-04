# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('importer', '0003_auto_20170104_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimportmap',
            name='type',
            field=models.CharField(max_length=120, default='Generic Product', help_text='Product Type değeri yazılacak, Örneğin: "Generic Product"'),
        ),
    ]
