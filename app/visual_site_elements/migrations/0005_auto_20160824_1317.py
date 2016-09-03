# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visual_site_elements', '0004_auto_20160822_1952'),
    ]

    operations = [
        migrations.AddField(
            model_name='promotion',
            name='slug',
            field=models.SlugField(blank=True),
        ),
        migrations.AlterField(
            model_name='promotionthumbnail',
            name='type',
            field=models.CharField(default='lg', choices=[('lg', 'Large'), ('md', 'Medium'), ('micro', 'Micro')], max_length=20),
        ),
    ]
