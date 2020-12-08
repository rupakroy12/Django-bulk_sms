from sms_portal.views import get_sms_reports_history
from django.contrib import admin
from django.urls import path, include
from sms_portal import views



urlpatterns = [
    path('', views.sms, name="sms"),
    path('sms_reports/', views.get_sms_reports_history, name = 'sms_reports'),
    path('read_csv/', views.read_csv, name='read_csv'),
    
]
