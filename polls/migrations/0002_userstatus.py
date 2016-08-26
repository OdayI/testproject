# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-26 22:05
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=200)),
                ('status_date', models.DateTimeField(default=datetime.datetime.now)),
                ('user_id', models.IntegerField(default=0)),
            ],
        ),
    ]