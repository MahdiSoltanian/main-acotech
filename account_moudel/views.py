from random import random
from django.urls import reverse
from django.views import View
from account_moudel.forms import RegisterForm
from account_moudel.models import User
from django.shortcuts import render, redirect
from django.shortcuts import render
from django.http import JsonResponse
from .sms_utils import send_verification_code
import random


'----------------------------------------------------------'
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

'----------------------------------------------------------'
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

'----------------------------------------------------------'
def send_code_view(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')  # دریافت شماره تلفن
        code = random.randint(100000, 999999)  # تولید کد ۶ رقمی تصادفی
        # ذخیره کد در دیتابیس یا کش (برای بررسی در مرحله بعد)
        request.session['verification_code'] = code
        send_verification_code(phone_number, code)
        return JsonResponse({'status': 'success', 'message': 'کد تایید ارسال شد'})
    return JsonResponse({'status': 'error', 'message': 'روش ارسال نامعتبر است'})

'----------------------------------------------------------'
def verify_code_view(request):
    if request.method == 'POST':
        entered_code = request.POST.get('code')  # کدی که کاربر وارد کرده
        original_code = request.session.get('verification_code')  # کدی که ذخیره شده
        if str(entered_code) == str(original_code):
            return JsonResponse({'status': 'success', 'message': 'کد تایید شد'})
        return JsonResponse({'status': 'error', 'message': 'کد اشتباه است'})
    return JsonResponse({'status': 'error', 'message': 'روش ارسال نامعتبر است'})
'----------------------------------------------------------'


