# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-24 10:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0002_auto_20160624_0953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='/media/Y/m/d'),
        ),
    ]
