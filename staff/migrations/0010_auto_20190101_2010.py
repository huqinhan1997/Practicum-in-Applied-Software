# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-01-01 20:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0009_decide'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Decide',
            new_name='Apply',
        ),
    ]
