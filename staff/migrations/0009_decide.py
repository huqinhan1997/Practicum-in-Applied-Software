# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-01-01 20:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0008_auto_20190101_1958'),
    ]

    operations = [
        migrations.CreateModel(
            name='Decide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staffname', models.CharField(db_column='申请人', max_length=64)),
                ('staffid', models.CharField(db_column='申请人编号', max_length=32)),
                ('clubname', models.CharField(db_column='申请社团', max_length=64)),
                ('clubid', models.CharField(db_column='社团编号', max_length=32)),
                ('a_time', models.DateTimeField(auto_now_add=True, db_column='申请时间')),
            ],
        ),
    ]
