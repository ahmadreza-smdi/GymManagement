from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.

class Time_option(models.Model):
    timee = models.CharField(max_length = 10)

    def __str__(self):
            return self.timee

class Fields(models.Model):
    name = models.CharField(max_length = 200)
    def __str__(self):
        return self.name


class F_t(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateField(auto_now=datetime.datetime.now())
    Field = models.ForeignKey(Fields, on_delete=models.CASCADE)
    time_options = models.ForeignKey(Time_option, on_delete=models.CASCADE)





class Member(models.Model):  
    sexuality = (
        ('M','male'),
        ('F','female'),
        ('O','other'),
    )
    skills = (
        ('‌‌B','beginner'),
        ('E','elementary'),
        ('P','professional'),
    )
    name = models.CharField(max_length = 200)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    phone_number = models.CharField(max_length = 11)
    field = models.ForeignKey(Fields,on_delete=models.CASCADE)
    birth_date = models.DateTimeField()
    first_session_date = models.DateTimeField(auto_now=True)
    sex = models.CharField(max_length =1 ,choices=sexuality)
    age = models.IntegerField()
    skill = models.CharField(max_length=1,choices = skills)
    profile = models.TextField(max_length = 200)   
    class_time = models.ForeignKey(Time_option,on_delete=models.CASCADE) 

    def __str__(self):
        return self.name