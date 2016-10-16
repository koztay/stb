# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('importer', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productimportmap',
            name='file',
        ),
        migrations.AddField(
            model_name='productimportmap',
            name='type',
            field=models.CharField(max_length=120, default='Projeksiyon Cihazı'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='fields',
            name='product_field',
            field=models.CharField(max_length=20, blank=True, choices=[('PRODUCT_TITLE', 'title'), ('PRODUCT_DESCRIPTION', 'description'), ('PRODUCT_CATEGORY', 'category'), ('PRODUCT_IMAGE', 'image')], null=True),
        ),
    ]
