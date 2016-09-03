# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import visual_site_elements.models


class Migration(migrations.Migration):

    dependencies = [
        ('visual_site_elements', '0006_horizontalbanner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name_of_person', models.CharField(max_length=120)),
                ('comment', models.CharField(max_length=500)),
                ('image', models.ImageField(upload_to=visual_site_elements.models.image_upload_to)),
                ('url', models.CharField(max_length=250)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]
