# Generated by Django 5.1.3 on 2024-11-28 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_moudel', '0017_alter_user_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_active_code',
            field=models.CharField(max_length=18, null=True),
        ),
    ]