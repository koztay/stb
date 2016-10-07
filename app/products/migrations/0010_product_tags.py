# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('products', '0009_auto_20160828_1758'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='tags',
            field=taggit.managers.TaggableManager(through='taggit.TaggedItem', to='taggit.Tag', help_text='A comma-separated list of tags.', verbose_name='Tags'),
        ),
    ]