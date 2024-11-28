from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=18)
    password = models.CharField(max_length=100)
    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

class OTP(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=6)  # کد ۶ رقمی
    created_at = models.DateTimeField(auto_now_add=True)

    def is_valid(self):
        return datetime.now() < self.created_at + timedelta(minutes=5)  # اعتبار کد ۵ دقیقه