# Generated by Django 3.2.8 on 2021-11-18 20:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Oracle', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='datestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 19, 1, 33, 42, 251130), null=True),
        ),
        migrations.AlterField(
            model_name='billing',
            name='datestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 19, 1, 33, 42, 257126), null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='city',
            field=models.CharField(blank=True, default='None', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='country',
            field=models.CharField(blank=True, default='None', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='dob',
            field=models.DateField(blank=True, default=datetime.datetime.now, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='email',
            field=models.CharField(blank=True, default='None', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='fname',
            field=models.CharField(blank=True, default='None', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='housestreet',
            field=models.CharField(blank=True, default='None', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='lname',
            field=models.CharField(blank=True, default='None', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='mobile',
            field=models.CharField(blank=True, default='None', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='salary',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
