from django.http import JsonResponse
from api_moudel.models import Data

def display_data(request):
    data = Data.objects.order_by('-id')[:10]  # Get the latest 10 records
    response = {
        "api_Key_Name": [temp.api_Key_Name for temp in data],
        "sensor_Name": [temp.value for temp in data],
        "temp": [temp.value for temp in data],
    }
    return JsonResponse(response)
    return render(request, 'flot.html')

