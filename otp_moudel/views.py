from django.shortcuts import render
from django.http import JsonResponse
from .sms_utils import send_verification_code
import random
from account_moudel.templates import *
def send_code_view(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')  # دریافت شماره تلفن
        code = random.randint(100000, 999999)  # تولید کد ۶ رقمی تصادفی
        # ذخیره کد در دیتابیس یا کش (برای بررسی در مرحله بعد)
        request.session['verification_code'] = code
        send_verification_code(phone_number, code)
        return JsonResponse({'status': 'success', 'message': 'کد تایید ارسال شد'})
    return JsonResponse({'status': 'error', 'message': 'روش ارسال نامعتبر است'})

def verify_code_view(request):
    if request.method == 'POST':
        return render(request,'varify.html')
        entered_code = request.POST.get('code')  # کدی که کاربر وارد کرده
        original_code = request.session.get('verification_code')  # کدی که ذخیره شده
        if str(entered_code) == str(original_code):
            return JsonResponse({'status': 'success', 'message': 'کد تایید شد'})
        return JsonResponse({'status': 'error', 'message': 'کد اشتباه است'})
    return JsonResponse({'status': 'error', 'message': 'روش ارسال نامعتبر است'})

