from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=18)
    password = models.CharField(max_length=100)
    phone_active_code = models.CharField(null=True,max_length=18)
    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
