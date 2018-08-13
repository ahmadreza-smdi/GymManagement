# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-11 10:41
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('web_athlete', '0025_auto_20180805_0743'),
    ]

    operations = [
        migrations.CreateModel(
            name='F_t',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_athlete.Fields')),
                ('time_options', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_athlete.Time_option')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
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
