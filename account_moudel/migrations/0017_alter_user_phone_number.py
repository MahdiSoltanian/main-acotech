# Generated by Django 5.1.3 on 2024-11-28 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_moudel', '0016_remove_user_email_active_code_user_phone_active_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(max_length=18),
        ),
    ]
