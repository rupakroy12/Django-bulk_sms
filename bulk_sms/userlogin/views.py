from sms_portal.scripts import send_sms
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from userlogin.models import credits
from django.contrib.auth import *
import django
# Create your views here.

def index(request) :
    return redirect(login)


def login(request):
    
    if request.method=="POST":
        username= request.POST.get('username')
        password= request.POST.get('password')
     
       
        #username and password validation
        user = authenticate(username = username, password = password)

        if user is not None:
            django.contrib.auth.login(request, user)
            return redirect("sms")
        else:
            return HttpResponse("<h1> Authentication failed </h1>")

    else:    
        return render(request,'login.html')



def signup(request):

    if request.method == "POST":

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        username = request.POST['username']

        if password==confirm_password:
            
            if User.objects.filter(username = username).exists():
                return HttpResponse("<h1>Username :'{}' exists already</h1>".format(first_name))
                
            else:
                us = User.objects.create_user(username = username, password = password, first_name = first_name, last_name = last_name, email=email)
                us.save() 

                cred = credits(user = us)
                # cred.username = user
                cred.save()
                return redirect("login")

        else: 
            print ("Password not matching")
            return HttpResponse("<h1> Password not Matching </h1>")
    else:
        return render(request, 'register.html')




def logout(request):
    print(request)
    django.contrib.auth.logout(request)
    return redirect("/")


def auth(request):
    return render(request,'auth_fail.html')
