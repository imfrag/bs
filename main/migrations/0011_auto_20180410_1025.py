# Generated by Django 2.0.3 on 2018-04-10 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_householder_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='image_description',
            field=models.ImageField(upload_to='house/'),
        ),
    ]
