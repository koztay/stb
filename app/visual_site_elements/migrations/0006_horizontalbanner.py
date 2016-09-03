# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import visual_site_elements.models


class Migration(migrations.Migration):

    dependencies = [
        ('visual_site_elements', '0005_auto_20160824_1317'),
    ]

    operations = [
        migrations.CreateModel(
            name='HorizontalBanner',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(max_length=120)),
                ('image', models.ImageField(upload_to=visual_site_elements.models.image_upload_to)),
                ('url', models.CharField(max_length=250)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]
