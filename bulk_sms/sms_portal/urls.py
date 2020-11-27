from django.contrib import admin
from django.urls import path, include
from sms_portal import views



urlpatterns = [
    path('', views.sms, name="sms"),
   
    
]
