from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth import authenticate,logout,login
from .models import Member,Fields,Time_option
from django.contrib.auth.models import User
import threading
from django.utils import timezone 
# from web_athlete.models import Class_times 

# Create your views here.
def loging(username,request,action):
    now = timezone.now() 
    f = open('log.txt','a+')
    f.write('username = %s , time = %s , action = %s \n'%(username,now,action))
    f.close()
    print('DONE')
    

def main(request):
    if request.method == 'GET':
        pass
    return render(request,'index.html')

def loginn(request):
    username = request.user.username
    if request.method == 'POST':
        username=request.POST.get('username','')
        print("username:",username)
        password=request.POST.get("password",'')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            loging(username,request,'log in')
            return HttpResponseRedirect('/dashboard')
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
        loging(username,request,'Regstration')

        return HttpResponseRedirect('/login/')
       
    return render(request,'Signup.html')

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
            loging(username,request,'Chosen time has updated')
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
            loging(username,request,'Settings has updated')
        return HttpResponseRedirect('/dashboard')
    if request.method == 'GET':
        return render(request,'settings.html',{'p':p})


def logout_view(request):  
    username = request.user.username  
    logout(request)
    loging(username,request,'log out')
    return HttpResponseRedirect('/login/')