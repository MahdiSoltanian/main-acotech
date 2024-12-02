from django.urls import path, include
from . import views

urlpatterns = [
    path('verify_code/', views.verify_code_view, name='register_page'),

]
