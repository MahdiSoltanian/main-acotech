from django.http import JsonResponse
from django.shortcuts import render

from api_moudel.models import Data


def display_data(request):
    data = Data.objects.order_by('-id')[:10]
    print(data)
    context = {
        "api_Key_Name": [temp.api_Key_Name for temp in data],
        "sensor_Name": [temp.sensor_Name for temp in data],
        "temp": [temp.temp for temp in data]
    }
    return render(request, 'flot.html',context)

