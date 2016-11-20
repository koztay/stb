# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='desi',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='product',
            name='kdv',
            field=models.IntegerField(default=18),
        ),
    ]
