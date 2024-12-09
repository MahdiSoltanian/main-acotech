from django.urls import path, include
from . import views

urlpatterns = [
    path('show/', views.display_data, name='admin-page')
]
