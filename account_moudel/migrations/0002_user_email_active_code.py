# Generated by Django 4.2.4 on 2024-01-29 09:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('account_moudel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email_active_code',
            field=models.CharField(default=123, max_length=100),
            preserve_default=False,
        ),
    ]
