# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-25 09:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0006_team_mate_one'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='mate_one',
        ),
    ]
