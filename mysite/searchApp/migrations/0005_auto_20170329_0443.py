# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-29 04:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchApp', '0004_auto_20170327_1012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insertcode',
            name='codeReview',
            field=models.BooleanField(),
        ),
    ]