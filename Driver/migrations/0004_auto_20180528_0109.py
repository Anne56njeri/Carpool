# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-27 22:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Driver', '0003_passenger_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passenger',
            name='Reviews',
            field=models.CharField(blank=True, max_length=40),
        ),
    ]
