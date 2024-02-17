from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from account_moudel.models import User


def profile_view(request):
    phone_number = request.session.get('phone_number')
    if phone_number:
        return render(request, 'index.html', {'phone_number': phone_number})
        print(phone_number)
    else:
        return redirect('admin-account')
