from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'', views.RZViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('redzone/',include(router.urls)),
    path('addredzone/', views.loadRedZoneData, name='loadRedZones'),
    path('nearestredzone/', views.nearestRedZone, name='nearestRedZone'),
]