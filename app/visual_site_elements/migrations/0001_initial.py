# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import visual_site_elements.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SliderImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('sub_title', models.CharField(max_length=50)),
                ('campaign', models.CharField(max_length=20)),
                ('image', models.ImageField(upload_to=visual_site_elements.models.image_upload_to)),
            ],
        ),
    ]
