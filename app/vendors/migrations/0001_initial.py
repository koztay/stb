# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_auto_20170104_1602'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tedarikci',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('unvan', models.CharField(max_length=120)),
                ('adres', models.TextField(blank=True, null=True)),
                ('telefon', models.CharField(blank=True, max_length=120, null=True)),
                ('fax', models.CharField(blank=True, max_length=120, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('vergi_dairesi', models.CharField(max_length=120)),
                ('vergi_no', models.CharField(max_length=120)),
                ('urunler', models.ManyToManyField(blank=True, to='products.Variation', null=True)),
            ],
        ),
    ]
