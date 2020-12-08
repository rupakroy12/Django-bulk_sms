from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime

# Create your models here.


class credits(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    credit_balance = models.IntegerField(default=10)
   
    
    def __str__(self):
        return self.user.username
    
    def get_credit(self):
        return self.credit_balance

    def update_credit(self):
        #decrement available credits by 1 after successful message sending.
        self.credit_balance-=1



class message_reports(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ret = models.BooleanField()
    status_code = models.IntegerField(null=True)
    request_id = models.CharField(max_length = 50, null=True)
    message = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        print (self.date)
        return self.user.username
