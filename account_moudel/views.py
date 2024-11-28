import http
from sms_ir import SmsIr

from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from .forms import RegisterForm, LoginForm
from .models import User
from django.utils.crypto import get_random_string


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

def verify_number(request):
    if request.method == 'POST':
        code = request.POST.get('verification_code')
        sms_ir = SmsIr(
            api_key="wRNDA4QMO2I1S75PaIXEhupIugrpWjIAsDPjOzi1jNGfSHGg",
        
            linenumber= 30007487129352,
        )
        sms_ir.send_verify_code(
        number="phone_number",
        template_id=10000,
        parameters=[
            {
            "CODE" : "CODE",
            "value": "12345"
            }
        ]
    )

        return HttpResponse("Code submitted: " + code)
    return render(request, 'varify.html')

