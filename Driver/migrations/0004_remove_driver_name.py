# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-21 20:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Driver', '0003_car_driver'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='driver',
            name='name',
        ),
    ]
