# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StaticPage',
            fields=[
                ('post_ptr', models.OneToOneField(serialize=False, auto_created=True, to='blog.Post', parent_link=True, primary_key=True)),
            ],
            bases=('blog.post',),
        ),
    ]
