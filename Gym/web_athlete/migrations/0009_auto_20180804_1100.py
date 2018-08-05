# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-04 11:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web_athlete', '0008_class_times_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Times',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timee', models.CharField(max_length=10)),
            ],
        ),
        migrations.RemoveField(
            model_name='class_times',
            name='chosen_time',
        ),
        migrations.AlterField(
            model_name='fields',
            name='class_time',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_athlete.Class_times'),
        ),
        migrations.AlterField(
            model_name='member',
            name='field',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_athlete.Fields'),
        ),
    ]
