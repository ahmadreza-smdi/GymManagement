# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-05 06:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web_athlete', '0022_auto_20180805_0616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='class_time',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_athlete.Time_option'),
        ),
        migrations.AlterField(
            model_name='member',
            name='field',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_athlete.Fields'),
        ),
    ]
