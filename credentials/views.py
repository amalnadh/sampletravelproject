from django.contrib import messages, auth
from django.contrib.auth.models import User



# Create your views here.
from django.shortcuts import redirect, render
def login (request):
    if request.method=='POST':
        uname=request.POST['uname']
        psw=request.POST['psw']
        user=auth.authenticate(username=uname,password=psw)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid credentilas")
            return redirect('login')



    return render(request,'login.html')

def register (request):
    if request.method=='POST':
        uname=request.POST['name']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email=request.POST['email']
        psw=request.POST['psw']
        repsw=request.POST['psw-repeat']

        if psw==repsw:
            if User.objects.filter(username=uname).exists():
                messages.info(request,"username already exists")
                return redirect('register')
            if User.objects.filter(email=email).exists():
                messages.info(request,"email already exists")
                return redirect('register')


            else:
                user=User.objects.create_user(username=uname,password=psw,first_name=fname,last_name=lname,email=email)
                user.save();
                return redirect('login')

            messages.info(request,'user created')
        else:
            messages.info(request,"password not matching")
            return redirect('register')
        return redirect('/')
    return render(request , "register.html")

def logout (request):
    auth.logout(request)
    return redirect('/')
