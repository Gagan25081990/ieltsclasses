# Generated by Django 2.0.1 on 2020-02-21 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ieltsapp', '0024_auto_20200221_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batch_db',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='blog_category_db',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='blog_db',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='course_db',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='main_course_category_db',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
