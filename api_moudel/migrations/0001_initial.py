# Generated by Django 5.1.3 on 2024-12-03 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('api_Key_Name', models.CharField(max_length=300)),
                ('sensor_Name', models.TextField()),
                ('temp', models.IntegerField(default=1)),
            ],
            options={
                'db_table': 'acotechi_data',
            },
        ),
    ]
