# Generated by Django 2.0.1 on 2020-03-06 07:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ieltsapp', '0033_auto_20200304_1119'),
    ]

    operations = [
        migrations.AddField(
            model_name='sub_course_category_db',
            name='sub_title',
            field=models.CharField(default=django.utils.timezone.now, max_length=10000),
            preserve_default=False,
        ),
    ]