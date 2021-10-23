# Generated by Django 3.2.8 on 2021-10-23 19:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Oracle', '0003_auto_20211023_2349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='datestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 24, 0, 4, 50, 831598), null=True),
        ),
        migrations.AlterField(
            model_name='billing',
            name='datestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 24, 0, 4, 50, 835603), null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='profile_pic',
            field=models.ImageField(default='clients/linuxghost.jpg', null=True, upload_to='clients'),
        ),
    ]