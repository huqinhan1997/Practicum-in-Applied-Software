# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-01-02 21:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0012_auto_20190102_2033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='date',
            field=models.DateField(db_column='活动时间'),
        ),
        migrations.AlterField(
            model_name='join',
            name='date',
            field=models.DateField(auto_now_add=True, db_column='参加日期'),
        ),
    ]
