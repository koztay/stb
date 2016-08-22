# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visual_site_elements', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sliderimage',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='sliderimage',
            name='url',
            field=models.CharField(max_length=250, default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='sliderimage',
            name='campaign',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='sliderimage',
            name='sub_title',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='sliderimage',
            name='title',
            field=models.CharField(max_length=120),
        ),
    ]
