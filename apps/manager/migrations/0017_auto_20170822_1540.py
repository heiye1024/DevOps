# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-22 07:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0016_auto_20170822_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='host',
            name='hostname',
            field=models.CharField(default='newhost.localhost', max_length=50),
        ),
    ]