# Generated by Django 2.0.1 on 2020-02-24 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ieltsapp', '0029_remove_student_notification_db_batch'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_notification_db',
            name='batch',
            field=models.ManyToManyField(blank=True, null=True, to='ieltsapp.Batch_Db'),
        ),
    ]