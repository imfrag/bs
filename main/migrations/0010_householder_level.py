# Generated by Django 2.0.3 on 2018-04-07 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20180323_1216'),
    ]

    operations = [
        migrations.AddField(
            model_name='householder',
            name='level',
            field=models.BooleanField(default=False),
        ),
    ]
