# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-12-16 10:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='ZIP_code',
            field=models.CharField(blank=True, max_length=6),
        ),
        migrations.AlterField(
            model_name='profile',
            name='adress',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='profile',
            name='city',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
