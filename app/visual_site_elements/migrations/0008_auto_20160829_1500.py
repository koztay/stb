# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('visual_site_elements', '0007_testimonial'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimonial',
            name='comment_date',
            field=models.DateField(default=datetime.datetime(2016, 8, 29, 15, 0, 10, 635172, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='image',
            field=models.CharField(max_length=500),
        ),
    ]
