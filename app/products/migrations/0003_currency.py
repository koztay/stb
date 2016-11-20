# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20161120_1435'),
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(default='₺', max_length=10, choices=[('₺', 'TL'), ('$', 'USD'), ('€', 'EUR')])),
                ('updated', models.DateField(auto_now=True)),
                ('value', models.FloatField(default=1.0)),
            ],
        ),
    ]
