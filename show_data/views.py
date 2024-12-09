from django.shortcuts import render
from api_moudel.models import Data

def display_data(request):
    data = Data.objects.all().order_by('-temp')  # Get all records, ordered by timestamp
    return render(request, 'flot.html', {'data': data})
