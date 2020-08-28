# Generated by Django 2.0.1 on 2020-02-05 06:56

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ieltsapp', '0018_auto_20200204_1126'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_profile',
            name='city',
            field=models.CharField(default=datetime.datetime(2020, 2, 5, 6, 55, 53, 687196, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user_profile',
            name='country',
            field=models.CharField(default=datetime.datetime(2020, 2, 5, 6, 56, 1, 861562, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
    ]