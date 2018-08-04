from django.db import models

# Create your models here.
class class_times(models.Model):
    open_times = (
        ('1','8 - 10'),
        ('2','10 - 12'),
        ('3','16 - 18'),
        ('4','18 - 20'),
    )
    chosen_time = models.CharField(max_length = 1, choices =open_times)
    def __str__(self):
        return self.open_times

class fields(models.Model):
    name = models.CharField(max_length = 200)
    class_time = models.ForeignKey(class_times,on_delete=models.CASCADE)
    def __str__(self):
        return self.name
class member(models.Model):   
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
    def __str__(self):
        return self.name