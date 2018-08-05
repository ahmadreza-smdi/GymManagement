from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth import authenticate,logout,login
from .models import Member,Fields,Time_option
from django.contrib.auth.models import User
# from web_athlete.models import Class_times 

# Create your views here.


def main(request):
    if request.method == 'GET':
        pass
    return render(request,'index.html')



def loginn(request):
    if request.method == 'POST':
        username=request.POST.get('username','')
        print("username:",username)
        password=request.POST.get("password",'')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
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
        Member.objects.filter(user__username=username).update(class_time=Open_times)
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
        Member.objects.filter(user__username=username).update(name = name ,phone_number =phone_number,sex = Sex,age = Age, skill = Skill ,profile = Bio )
        return HttpResponseRedirect('/dashboard')
    if request.method == 'GET':
        return render(request,'settings.html',{'p':p})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/login/')