# Generated by Django 2.0 on 2018-03-17 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20180306_1950'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='size',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='car',
            name='car_number',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
