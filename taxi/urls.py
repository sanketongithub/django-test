from django.contrib import admin
from django.urls import path
from . import views
from .views import send_json


urlpatterns = [
    path('index/', views.index),
    path('scookie/',views.setcookie),
    path('gcookie/',views.getcookie),
    path('testurl',views.testurl),
    path('pathtoredirect/<int:args>/',views.pathtoredirect,name='redirectpath'),
    path('carinfo',views.carinfo),
    path('sendjson/', send_json, name='send_json'),
]