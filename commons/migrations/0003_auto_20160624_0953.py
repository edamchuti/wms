# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-24 09:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commons', '0002_auto_20160624_0801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
    ]