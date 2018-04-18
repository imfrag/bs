# Generated by Django 2.0.3 on 2018-04-18 16:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20180410_1025'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('bill_id', models.AutoField(primary_key=True, serialize=False)),
                ('bill_description', models.CharField(max_length=50)),
                ('bill_money', models.FloatField()),
                ('bill_receive', models.CharField(max_length=10)),
                ('bill_pay', models.CharField(max_length=10)),
                ('bill_createtime', models.TimeField(verbose_name=django.utils.timezone.now)),
                ('bill_paytime', models.TimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'bill',
            },
        ),
    ]