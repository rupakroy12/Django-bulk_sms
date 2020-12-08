from sms_portal.scripts import send_sms, write_file
from django.shortcuts import render, redirect
from django.http import HttpResponse
<<<<<<< HEAD
from django.contrib.auth.models import User
from userlogin.models import credits, message_reports

import csv
# from scripts import 
# import scripts
=======
from .scripts import *
>>>>>>> ee7a3d771593bdd8eb7ce062c3c7be874d9f56fb

# Create your views here.


def sms(request):
    if request.method == "POST":
        
        current_user = request.user.id
        obj = credits.objects.filter(user=current_user)[0]

        #if credits is not 0 then user can send sms else not
        if (obj.get_credit() > 0) :
            message = request.POST["message"]
            number = request.POST["number"]
            number = number.replace("\r\n", ",")
            print(type(number))

            print(number)
            dict = send_sms(number, message)
            print(dict)

            #updating user credits
            if dict.get('return'):
                obj.update_credit()
                obj.save()

            #updating reports
            reports = message_reports(ret = dict.get('return'), status_code = dict.get('status_code'), message = dict.get('message'), request_id = dict.get('request_id') ,user = request.user)
            reports.save()

            return render(request, 'report.html', {'reports': dict })
        
        #if credits equal 0 then user cannot send sms
        else:
            return HttpResponse("<h1> Insufficient Credits </h1>")

    #For request.method='GET'
    else:
        if request.user.is_authenticated:
            current_user = request.user.id
            obj = credits.objects.filter(user = current_user)
            
            if obj is not None:
                credit =  obj[0].get_credit()
            else :
                credit = 0 

            return render(request, "send_sms.html", context = {'credit':credit})
        else:
            return render(request, "send_sms.html")


def get_sms_reports_history(request):
    reports = message_reports.objects.filter(user=request.user.id)
    report_lst = {}
    i = len(reports)

    for report in reports:
        dic = {}
        dic["return"] = report.ret
        dic["request_id"] = report.request_id
        dic["message"] = report.message
        dic["status_code"] = report.status_code
        dic["date"] = report.date


        report_lst[i]=dic
        i-=1
    
    # report = report_lst
    report = dict(reversed(list(report_lst.items())))
    print(report)

    return render(request,'sent_sms_reports.html', {'report':report})


def read_csv(request):
       
    return HttpResponse("File received")
