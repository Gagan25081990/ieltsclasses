# Generated by Django 2.0.1 on 2019-12-25 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ieltsapp', '0002_auto_20191225_1137'),
    ]

    operations = [
        migrations.AddField(
            model_name='course_content_db',
            name='trash',
            field=models.BooleanField(default=1),
        ),
    ]
