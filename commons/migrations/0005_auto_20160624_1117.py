# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-24 11:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commons', '0004_auto_20160624_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='Telephone'),
        ),
    ]
