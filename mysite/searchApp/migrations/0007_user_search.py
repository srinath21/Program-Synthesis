# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-23 10:16
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('searchApp', '0006_auto_20170419_1341'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_Search',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='searchApp.Code')),
                ('query', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='searchApp.Query')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
