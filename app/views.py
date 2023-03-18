from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from django.http import HttpResponse
from .models import RedZone
from .serializer import RZSerializer
import pandas as pd
import numpy as np
# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class RZViewSet(viewsets.ModelViewSet):
    queryset = RedZone.objects.all().order_by('-id')
    serializer_class = RZSerializer

@api_view(['get'])
def loadRedZoneData(request):
    
    dataset = pd.read_csv('nepalmonitor-reports (4).csv', encoding= 'unicode_escape')

    RedZone.objects.all().delete()
    print(dataset)
    for i in range(len(dataset)):
        # print(dataset.iloc[i].Address)
        redZone = RedZone(
          latitude=dataset.iloc[i].Latitude,
          longitude = dataset.iloc[i].Longitude,
          location= dataset.iloc[i].Location
        )
        redZone.save()
    return Response("redzone are Added")

@api_view(['POST'])
def nearestRedZone(request):
  userData = request.data
  longitude = userData['longitude'] 
  latitude = userData['latitude']
  
  redzone = RedZone.objects.all()
  serializer = RZSerializer(redzone, many=True,context={'request': request})
  loc = []
  rzData=[]
  # print(serializer.data[58])
  for i in range(len(serializer.data)):
      # print(i)
      # print(serializer.data[i]['id'])
      la=(latitude-serializer.data[i]['latitude'])**2
      lo=(longitude-serializer.data[i]['longitude'])**2

      loc.append([serializer.data[i]['id'], np.sqrt(la+lo)])

  loc.sort(key = lambda row: row[1])
  # print(loc)
  for i in range(len(serializer.data)):
     if serializer.data[i]['id'] == loc[0][0] :
        rzData = serializer.data[i]
  
  # print(dataset.iloc[loc[0][0]-1].Address)
  # print(rzData)
  location = {
    "id": rzData["id"],
    "location": rzData["location"],
    "longitude": rzData['longitude'],
    "latitude": rzData['latitude']
  }
  return Response(location)