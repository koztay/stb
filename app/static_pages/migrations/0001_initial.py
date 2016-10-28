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
                ('post_ptr', models.OneToOneField(auto_created=True, parent_link=True, serialize=False, primary_key=True, to='blog.Post')),
            ],
            bases=('blog.post',),
        ),
    ]
