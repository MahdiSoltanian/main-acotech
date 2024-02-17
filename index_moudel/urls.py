from django.urls import path,include
from . import views

urlpatterns = [
    path('account_admin/',views.profile_view,name='admin-page')
]