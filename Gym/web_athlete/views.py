from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth import authenticate,logout,login
from .models import Member,Fields,Time_option
from django.contrib.auth.models import User
import threading
from log_package import logg
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone 

def main(request):
    if request.method == 'GET':
        pass
    return render(request,'index.html')

def loginn(request):
    if request.method == 'POST':
        username=request.POST.get('username','')
        print("username:",username)
        password=request.POST.get("password",'')
        print("password",password)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            print("login is true")
            logg.loging(username,request,'login')
            return HttpResponseRedirect('/dashboard')
        else:
            print("login is false")
            return HttpResponseRedirect('/login/')

    return render(request,'Signin.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            logg.loging(username,request,'register')

        return HttpResponseRedirect('/login/')
    else:
        form = UserCreationForm()
    return render(request,'Signup.html',{'form':form})

def dashboard(request):
    username = None
    if request.user.is_authenticated():
        username = request.user.username
    return render(request,'dashboard.html',{"user_name":username})



def choose_time(request):
    username = request.user.username
    if request.method == 'POST':
        Open_times=request.POST.get('time_select')
        a = Member.objects.filter(user__username=username).update(class_time=Open_times)
        if a :
            logg.loging(username,request,'Chosen time has updated')
        return HttpResponseRedirect('/dashboard')

    print (username)
    t = Time_option.objects.all()
    return render(request,'time.html',{'t':t})

def settings(request):
    username = request.user.username
    p = Member.objects.get(user__username = username)
    print(p.phone_number)
    if request.method == 'POST':
        username = request.user.username
        name=request.POST.get('name')
        Skill=request.POST.get('Skill')
        Age=request.POST.get('Age')
        phone_number=request.POST.get('phone_number')
        Sex=request.POST.get('Sex')
        Bio=request.POST.get('bio')
        birthdate=request.POST.get('birthdate')
        a = Member.objects.filter(user__username=username).update(name = name ,phone_number =phone_number,sex = Sex,age = Age, skill = Skill ,profile = Bio )
        if a:
            logg.loging(username,request,'Settings has updated')
        return HttpResponseRedirect('/dashboard')
    if request.method == 'GET':
        return render(request,'settings.html',{'p':p})


def logout_view(request):  
    username = request.user.username  
    logout(request)
    logg.loging(username,request,'logout')
    return HttpResponseRedirect('/login/')