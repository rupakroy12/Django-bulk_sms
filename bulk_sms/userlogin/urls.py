from django.contrib import admin
from django.urls import path, include
from userlogin import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', views.signup, name = "signup"),
    path('', views.index, name="index"),
    path('login/', views.login, name="login"),
    path('sms/logout/', views.logout, name="logout"),   
]
