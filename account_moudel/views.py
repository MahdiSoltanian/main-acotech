from random import random
from django.urls import reverse
from django.views import View
from rest_framework.views import APIView

from account_moudel.forms import RegisterForm
from account_moudel.models import User
from django.shortcuts import render, redirect
from django.shortcuts import render
from django.http import JsonResponse
from .sms_utils import send_verification_code
import random
from kavenegar import *


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
            return redirect('admin-page')  # Redirect to home page or any other page after login
        else:
            return render(request, 'login.html', {'error_message': 'Invalid username or password'})

    def get(self, request):
        return render(request, 'login.html')

'----------------------------------------------------------'
'''
class GenerateOTP(APIView):
    serializer_class = GetOTP

    def post(self, request, format=None):
        ser = self.serializer_class(
            data=request.data,
            context={'request': request}
        )
        if ser.is_valid():
            ...
            token = randint(100000, 999999)
            kave_negar_token_send(ser.data['phone_number'], token)
            ...

'----------------------------------------------------------'

API_KEY = '356F2F386B49427250374934354B4C4744475A6C4649452B6C6E74762F4D77635A6376612B4E4674586C303D'
def kave_negar_token_send(receptor, token):
    try:
        api = KavenegarAPI(API_KEY)
        params = {
            'receptor': receptor,
            'template': 'your_template',
            'token': token
        }
        response = api.verify_lookup(params)
    except APIException as e:
        print(e)
    except HTTPException as e:
        print(e)

token = random.randint(1000, 9999)
token = random.randint(10000, 99999)
token = random.randint(100000, 999999)
token = random.randint(1000, 9999)
kave_negar_token_send(ser.data['phone_number'], token)
'''