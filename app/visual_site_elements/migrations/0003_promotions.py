# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import visual_site_elements.models


class Migration(migrations.Migration):

    dependencies = [
        ('visual_site_elements', '0002_auto_20160822_1449'),
    ]

    operations = [
        migrations.CreateModel(
            name='Promotions',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('sub_title', models.CharField(max_length=80)),
                ('image', models.ImageField(upload_to=visual_site_elements.models.image_upload_to)),
                ('url', models.CharField(max_length=250)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]
