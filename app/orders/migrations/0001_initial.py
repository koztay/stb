# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('status', models.CharField(default='created', max_length=120, choices=[('created', 'Created'), ('paid', 'Paid'), ('shipped', 'Shipped'), ('refunded', 'Refunded')])),
                ('shipping_total_price', models.DecimalField(default=5.99, max_digits=50, decimal_places=2)),
                ('order_total', models.DecimalField(max_digits=50, decimal_places=2)),
                ('order_id', models.CharField(max_length=50, blank=True, null=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='UserAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('type', models.CharField(max_length=120, choices=[('billing', 'Billing'), ('shipping', 'Shipping')])),
                ('street', models.CharField(max_length=120)),
                ('city', models.CharField(max_length=120)),
                ('state', models.CharField(max_length=120)),
                ('zipcode', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='UserCheckout',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('email', models.EmailField(unique=True, max_length=254)),
                ('braintree_id', models.CharField(max_length=120, blank=True, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='useraddress',
            name='user',
            field=models.ForeignKey(to='orders.UserCheckout'),
        ),
        migrations.AddField(
            model_name='order',
            name='billing_address',
            field=models.ForeignKey(related_name='billing_address', null=True, to='orders.UserAddress'),
        ),
        migrations.AddField(
            model_name='order',
            name='cart',
            field=models.ForeignKey(to='carts.Cart'),
        ),
        migrations.AddField(
            model_name='order',
            name='shipping_address',
            field=models.ForeignKey(related_name='shipping_address', null=True, to='orders.UserAddress'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(to='orders.UserCheckout', null=True),
        ),
    ]
