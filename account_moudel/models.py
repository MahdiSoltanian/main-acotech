from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50)
    phone_number = models.IntegerField()
    password = models.CharField(max_length=100)
    email_active_code = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
