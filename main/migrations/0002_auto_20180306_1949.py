# Generated by Django 2.0 on 2018-03-06 19:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billboard',
            name='publish_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 6, 19, 49, 14, 37857)),
        ),
        migrations.AlterField(
            model_name='householder',
            name='register_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 6, 19, 49, 14, 33857)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='checkin_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 6, 19, 49, 14, 37857)),
        ),
        migrations.AlterField(
            model_name='relcarholder',
            name='checkin_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 6, 19, 49, 14, 41857)),
        ),
        migrations.AlterField(
            model_name='relhouseholder',
            name='checkin_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 6, 19, 49, 14, 41857)),
        ),
        migrations.AlterField(
            model_name='repair',
            name='publish_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 6, 19, 49, 14, 35857)),
        ),
    ]