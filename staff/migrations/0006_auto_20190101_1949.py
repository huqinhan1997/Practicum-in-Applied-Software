# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-01-01 19:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0005_auto_20190101_1948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='decide',
            name='cid',
            field=models.CharField(db_column='编号', max_length=32),
        ),
        migrations.AlterField(
            model_name='decide',
            name='sid',
            field=models.CharField(db_column='职工号', max_length=32),
        ),
        migrations.AlterField(
            model_name='decide',
            name='sname',
            field=models.CharField(db_column='姓名', max_length=64),
        ),
    ]
