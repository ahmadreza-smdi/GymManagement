from django.shortcuts import render,HttpResponseRedirect
from . import models
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
# Create your views here.


def main(request):
    if request.method == 'GET':
        pass
    return render(request,'index.html')



def login(request):
    if request.method == 'POST':
        username=request.POST.get('username','')
        print("username:",username)
        password=request.POST.get("password",'')
        user = authenticate(username=username, password=password)
        if user is not None:
           return HttpResponseRedirect('/register')
        else:
            return HttpResponseRedirect('/login/')

    return render(request,'Signin.html')


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        email = request.POST.get('email','')  
        new_save=User(username=username,password=password,email=email)
        new_save.save()
        return HttpResponseRedirect('/login/')
       
    return render(request,'Signup.html')