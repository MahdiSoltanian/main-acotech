from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from .models import Data
from .serializers import DataSerializer
from django.http import HttpResponse



@api_view(['GET','POST'])
def index(request:Request):
    if request.method =='GET':
        datas = Data.objects.order_by('temp').all()
        data_deserializer = DataSerializer(datas,many=True)
        return Response(data_deserializer.data,status.HTTP_200_OK)

    elif request.method == 'POST':
        data_serializer = DataSerializer(data=request.data)
        if data_serializer.is_valid():
            data_serializer.save()
            return Response(data_serializer.data,status.HTTP_201_CREATED)
            print(data_serializer)
        else:
            return Response(data_serializer.data, status.HTTP_200_OK)
            data_serializer.save()
            print(data_serializer)

@api_view(['GET',"PUT","DELETE"])
def data_detail(request:Request,Data_id):
    try:
        data = Data.objects.get(pk=Data_id)
    except Data.DoseNotExist:
        return Response(None,status.HTTP_404_NOT_FOUND)

