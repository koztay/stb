# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('importer', '0002_auto_20170104_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimportmap',
            name='root',
            field=models.CharField(null=True, blank=True, help_text='Eğer XML dosyası ise o zaman ürünlerin çekileceği root tagi yaz.', max_length=120),
        ),
    ]
