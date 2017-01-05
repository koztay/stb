# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('importer', '0004_auto_20170104_1905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fields',
            name='xml_field',
            field=models.CharField(max_length=1200, help_text='Buraya excel için index değerini yaz: 0,1,2 vb.XML için ne yazılacak bakacağız.', blank=True, null=True),
        ),
    ]
