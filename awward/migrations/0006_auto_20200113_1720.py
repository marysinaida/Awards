# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-01-13 14:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awward', '0005_auto_20200113_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_photo',
            field=models.ImageField(upload_to='profile/'),
        ),
    ]