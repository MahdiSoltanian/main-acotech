import http
from datetime import datetime
from random import random

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from sms_ir import SmsIr
from otp_moudel import templates

from account_moudel.forms import RegisterForm
from account_moudel.models import User


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

    import random
    import requests
    from django.http import JsonResponse
    from django.views.decorators.csrf import csrf_exempt
    from django.core.cache import cache

    # تنظیمات کاوه نگار
    KAVEHNEGAR_API_KEY = "your_kaveh_negar_api_key"  # کلید API کاوه نگار
    CACHE_TIMEOUT = 300  # زمان انقضا برای ذخیره کد تأیید در حافظه (ثانیه)

    def send_verification_code(phone_number):
        """
        ارسال کد تأیید به شماره موبایل
        """
        verification_code = random.randint(100000, 999999)  # تولید کد ۶ رقمی
        cache.set(phone_number, verification_code, CACHE_TIMEOUT)  # ذخیره کد در حافظه موقت

        url = f"https://api.kavenegar.com/v1/{KAVEHNEGAR_API_KEY}/sms/send.json"
        data = {
            "receptor": phone_number,
            "message": f"کد تأیید شما: {verification_code}"
        }
        response = requests.post(url, data=data)
        return response.json()

    @csrf_exempt
    def send_code_view(request):
        """
        ویوی ارسال کد تأیید
        """
        if request.method == "POST":
            phone_number = request.POST.get("phone_number")
            if not phone_number:
                return JsonResponse({"success": False, "message": "شماره موبایل ارسال نشده است."})

            response = send_verification_code(phone_number)
            if response.get("return", {}).get("status") == 200:
                return JsonResponse({"success": True, "message": "کد تأیید ارسال شد."})
            else:
                return JsonResponse({"success": False, "message": "ارسال پیامک با خطا مواجه شد."})
        return JsonResponse({"success": False, "message": "فقط درخواست POST پشتیبانی می‌شود."})

    @csrf_exempt
    def verify_code_view(request):
        """
        ویوی تأیید کد
        """
        if request.method == "POST":
            phone_number = request.POST.get("phone_number")
            entered_code = request.POST.get("code")

            if not phone_number or not entered_code:
                return JsonResponse({"success": False, "message": "اطلاعات کامل ارسال نشده است."})

            saved_code = cache.get(phone_number)
            if saved_code and str(saved_code) == str(entered_code):
                return JsonResponse({"success": True, "message": "کد تأیید صحیح است."})
            else:
                return JsonResponse({"success": False, "message": "کد تأیید نادرست است."})
        return JsonResponse({"success": False, "message": "فقط درخواست POST پشتیبانی می‌شود."})
