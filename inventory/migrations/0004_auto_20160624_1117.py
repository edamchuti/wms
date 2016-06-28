# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-24 11:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_auto_20160624_0953'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='incoming',
            options={'verbose_name': 'Return', 'verbose_name_plural': 'Returns'},
        ),
        migrations.AlterModelOptions(
            name='outgoing',
            options={'verbose_name': 'Borrow', 'verbose_name_plural': 'Borrows'},
        ),
        migrations.AlterField(
            model_name='incoming',
            name='amount',
            field=models.PositiveIntegerField(default=1, help_text="Let's just use 1 as a value to log better!"),
        ),
        migrations.AlterField(
            model_name='outgoing',
            name='amount',
            field=models.PositiveIntegerField(default=1, help_text="Let's just use 1 as a value to log better!"),
        ),
    ]
