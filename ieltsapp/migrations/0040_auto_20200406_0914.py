# Generated by Django 2.0.1 on 2020-04-06 09:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ieltsapp', '0039_live_db_live_notification_db'),
    ]

    operations = [
        migrations.AddField(
            model_name='live_db',
            name='live_date',
            field=models.CharField(default=datetime.datetime(2020, 4, 6, 9, 14, 40, 159456), max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='live_notification_db',
            name='live_date',
            field=models.CharField(default=datetime.datetime(2020, 4, 6, 9, 14, 48, 676130), max_length=1000),
            preserve_default=False,
        ),
    ]
