from django.urls import path, include
from . import views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register_page'),
    path('login/', views.loginview.as_view(), name='login_page'),
    #path('varify_number/',views.send_code_view,name='varify_number')
]
