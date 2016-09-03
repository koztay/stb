# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visual_site_elements', '0008_auto_20160829_1500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='comment',
            field=models.TextField(),
        ),
    ]
