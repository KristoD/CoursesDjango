# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-02-18 08:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='description',
            name='content',
            field=models.TextField(default=''),
        ),
    ]
