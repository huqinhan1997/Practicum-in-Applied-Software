# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-01-03 00:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0016_auto_20190103_0053'),
    ]

    operations = [
        migrations.CreateModel(
            name='Join',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('j_time', models.DateTimeField(auto_now_add=True, db_column='报名时间')),
                ('aid', models.ForeignKey(db_column='活动编号', on_delete=django.db.models.deletion.DO_NOTHING, to='staff.Activity')),
                ('sid', models.ForeignKey(db_column='职工号', on_delete=django.db.models.deletion.DO_NOTHING, to='staff.Staff')),
            ],
        ),
    ]
