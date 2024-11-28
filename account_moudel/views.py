import http
from datetime import datetime
from random import random

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from sms_ir import SmsIr

from account_moudel.forms import RegisterForm
from account_moudel.models import User, OTP


class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()

        context = {
            'register_form': register_form
        }

        return render(request, 'register.html', context)
    def post(self, request):
        register_form = RegisterForm(request.POST)

        if register_form.is_valid():
            user_phoneNumber = register_form.cleaned_data.get('phone_number')
            user_name = register_form.cleaned_data.get('name')
            user_password = register_form.cleaned_data.get('password')
            print(user_phoneNumber)
            user: bool = User.objects.filter(phone_number=user_phoneNumber).exists()
            if user:
                register_form.add_error('phone_number', 'this phone_number does exist')
            else:
                new_user = User(phone_number=user_phoneNumber, name=user_name,
                                password=user_password)

                new_user.save()
                return redirect(reverse('login_page'))
        context = {
            'register_form': register_form
        }

        return render(request, 'register.html', context)


from django.shortcuts import render, redirect


class loginview(View):

    def post(self, request):
        phone_number = request.POST.get('phone_number')
        password = request.POST.get('password')
        name = request.POST.get('name')
        #print(name)
        try:
            user = User.objects.get(phone_number=phone_number, password=password,name=name)
        except User.DoesNotExist:
            user = None
        if user is not None:
            request.session['phone_number'] = phone_number  # Store username in session
            request.session['name'] = name
            return redirect('varify_number')  # Redirect to home page or any other page after login
        else:
            return render(request, 'varify.html', {'error_message': 'Invalid username or password'})

    def get(self, request):
        return render(request, 'login.html')
from django.shortcuts import render
from django.http import HttpResponse




# تنظیمات پیامک
SMS_API_KEY = 'wRNDA4QMO2I1S75PaIXEhupIugrpWjIAsDPjOzi1jNGfSHGg'

def send_otp(user):
    otp_code = str(random.randint(100000, 999999))  # تولید کد ۶ رقمی
    otp, created = OTP.objects.get_or_create(user=user)
    otp.code = otp_code
    otp.created_at = datetime.now()
    otp.save()

    # ارسال پیامک
    sms = SmsIr(API_KEY=SMS_API_KEY)
    sms.send({'MobileNumbers': [user.profile.phone_number], 'Messages': [f"کد ورود شما: {otp_code}"]})

@login_required
def send_login_otp(request):
    user = request.user
    send_otp(user)
    return render(request, 'otp_sent.html')  # صفحه‌ای که به کاربر اطلاع دهد پیامک ارسال شده
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import OTP

@login_required
def verify_otp(request):
    if request.method == 'POST':
        user = request.user
        code = request.POST.get('otp')

        try:
            otp = OTP.objects.get(user=user, code=code)
            if otp.is_valid():
                messages.success(request, "ورود با موفقیت انجام شد!")
                return redirect('home')  # صفحه اصلی
            else:
                messages.error(request, "کد منقضی شده است.")
        except OTP.DoesNotExist:
            messages.error(request, "کد وارد شده نادرست است.")

    return render(request, 'verify_otp.html')
