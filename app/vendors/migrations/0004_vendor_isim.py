# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0003_auto_20170104_1623'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='isim',
            field=models.CharField(default='test vendor', max_length=120),
            preserve_default=False,
        ),
    ]
