# Generated by Django 4.2.1 on 2023-05-11 10:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('talkshop', '0004_rename_name_business_infosource_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='title',
        ),
    ]