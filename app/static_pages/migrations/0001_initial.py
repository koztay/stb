# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StaticPage',
            fields=[
                ('post_ptr', models.OneToOneField(serialize=False, primary_key=True, to='blog.Post', parent_link=True, auto_created=True)),
            ],
            bases=('blog.post',),
        ),
    ]
