# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-26 11:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0009_remove_team_mate_one'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='mate_one',
            field=models.CharField(default='none', max_length=20, verbose_name='\u961f\u5458\u4e00'),
        ),
    ]
