# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-01-01 19:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0007_m'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Decide',
        ),
        migrations.DeleteModel(
            name='M',
        ),
    ]
