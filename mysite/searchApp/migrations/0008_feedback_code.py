# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-23 10:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('searchApp', '0007_user_search'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='code',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to='searchApp.Code'),
            preserve_default=False,
        ),
    ]