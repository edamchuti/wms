# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-24 09:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='assetbrand',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='assetgroup',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
    ]
