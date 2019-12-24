# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-12-31 03:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('aid', models.CharField(db_column='编号', max_length=32, primary_key=True, serialize=False)),
                ('aname', models.CharField(db_column='名称', max_length=64)),
                ('manager', models.CharField(db_column='负责人', max_length=64)),
                ('location', models.CharField(db_column='活动地点', max_length=128)),
                ('date', models.CharField(db_column='活动时间', max_length=32)),
                ('nump', models.IntegerField(db_column='人数')),
            ],
        ),
        migrations.CreateModel(
            name='Club',
            fields=[
                ('cid', models.CharField(db_column='编号', max_length=32, primary_key=True, serialize=False, unique=True)),
                ('cname', models.CharField(db_column='名称', max_length=64)),
                ('manager', models.CharField(db_column='负责人', max_length=32)),
                ('location', models.CharField(db_column='活动地点', max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Decide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sid', models.CharField(db_column='职工号', max_length=32)),
                ('sname', models.CharField(db_column='姓名', max_length=64)),
                ('cid', models.CharField(db_column='编号', max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Join',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True, db_column='参加日期')),
                ('cid', models.ForeignKey(db_column='编号', on_delete=django.db.models.deletion.DO_NOTHING, to='staff.Club')),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('sid', models.CharField(db_column='职工号', max_length=32, primary_key=True, serialize=False, unique=True)),
                ('sname', models.CharField(db_column='姓名', max_length=64)),
                ('age', models.IntegerField(db_column='年龄')),
                ('gender', models.CharField(choices=[('男', '男'), ('女', '女')], db_column='性别', default='男', max_length=32)),
                ('c_time', models.DateTimeField(auto_now_add=True, db_column='注册时间')),
                ('password', models.CharField(db_column='登录密码', max_length=256)),
            ],
            options={
                'verbose_name': 'Staff',
                'verbose_name_plural': 'Staff',
                'ordering': ['-c_time'],
            },
        ),
        migrations.AddField(
            model_name='join',
            name='sid',
            field=models.ForeignKey(db_column='职工号', on_delete=django.db.models.deletion.DO_NOTHING, to='staff.Staff'),
        ),
        migrations.AddField(
            model_name='activity',
            name='cname',
            field=models.ForeignKey(db_column='社团', on_delete=django.db.models.deletion.DO_NOTHING, to='staff.Club'),
        ),
    ]
