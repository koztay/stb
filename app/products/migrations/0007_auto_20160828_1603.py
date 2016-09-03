# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20160824_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thumbnail',
            name='type',
            field=models.CharField(default='hd', choices=[('hd', 'HD'), ('sd', 'SD'), ('medium', 'Medium'), ('micro', 'Micro')], max_length=20),
        ),
    ]
