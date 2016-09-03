# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20160828_1758'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductView',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('count', models.IntegerField(default=0)),
                ('product', models.ForeignKey(to='products.Product')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, blank=True, null=True)),
            ],
        ),
    ]
