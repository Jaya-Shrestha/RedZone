from django.shortcuts import render
from rest_framework import viewsets
from django.http import HttpResponse
from .models import RedZone
from .serializer import RZSerializer

# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class RZViewSet(viewsets.ModelViewSet):
    queryset = RedZone.objects.all().order_by('-id')
    serializer_class = RZSerializer