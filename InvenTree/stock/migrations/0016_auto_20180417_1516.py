# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-17 15:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0015_auto_20180417_1514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockitem',
            name='notes',
            field=models.TextField(blank=True),
        ),
    ]