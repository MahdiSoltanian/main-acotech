# Generated by Django 3.2.8 on 2024-02-19 18:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account_moudel', '0014_user_user_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='user_image',
        ),
    ]
