# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-04 10:26
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('web_athlete', '0007_auto_20180801_0812'),
    ]

    operations = [
        migrations.AddField(
            model_name='class_times',
            name='username',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
