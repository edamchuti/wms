# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-24 10:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commons', '0003_auto_20160624_0953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='care_of_person',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='C/O'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]