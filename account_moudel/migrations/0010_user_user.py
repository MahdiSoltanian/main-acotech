# Generated by Django 4.2.4 on 2024-02-08 08:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('account_moudel', '0009_remove_user_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user',
            field=models.CharField(default=123, max_length=50),
            preserve_default=False,
        ),
    ]
