# Generated by Django 4.2.4 on 2024-02-08 08:21

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('account_moudel', '0008_user_user_alter_user_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='user',
        ),
    ]
