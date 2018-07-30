from django.db import models

# Create your models here.

class fields(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length = 200)


class user(models.Model):
    
    def __str__(self):
        return self.name
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
    phone_number = models.CharField(max_length = 11)
    field = models.ForeignKey(fields,on_delete=models.CASCADE)
    birth_date = models.DateTimeField()
    first_session_date = models.DateTimeField(auto_now=True)
    sex = models.CharField(max_length =1 ,choices=sexuality)
    age = models.IntegerField()
    skill = models.CharField(max_length=1,choices = skills)
    profile = models.TextField(max_length = 200)