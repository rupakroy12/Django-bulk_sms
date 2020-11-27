from sms_portal.scripts import send_sms, write_file
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .scripts import *

# Create your views here.

def sms(request):
    # return render(request, "send_sms.html")

# def get_sms(request):

    if request.method == "POST":
        message = request.POST["message"]
        number = request.POST["number"]
        number = number.replace("\r\n",",")
        print (type(number))
       
        print(number)
        dict = send_sms(number, message)
        print(dict)
        
        # writing records to csv
        # records = {}
        # records[number] = dict
        # write_file(records)

        return HttpResponse("<h1>{}</h1>".format(str(dict)))

    else :
        return render(request, "send_sms.html")

