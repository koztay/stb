from __future__ import absolute_import, unicode_literals
import random
from celery.decorators import task

from utils import kur_cek
from .models import Currency


@task(name="sum_two_numbers")
def add(x, y):
    return x + y


@task(name="multiply_two_numbers")
def mul(x, y):
    total = x * (y * random.randint(3, 100))
    return total


@task(name="sum_list_numbers")
def xsum(numbers):
    return sum(numbers)


@task(name="euro_cek")
def euro_cek(currency_name='EURO'):
    return kur_cek.get(currency_name)


@task(name="USD_cek")
def usd_cek(currency_name='ABD DOLARI'):
    return kur_cek.get(currency_name)

