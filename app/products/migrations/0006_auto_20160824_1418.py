# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20160824_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='order',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
