from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *

# THESE ARE THE LOGIN VIEWS
def index(request):
    if 'user_id' in request.session:
        request.session.clear()

    return render(request,"login_app/index.html")

def processing(request): # process for registering new users

    if request.method == "POST":
        errors = User.objects.basic_validator(request.POST)
        if len(errors): # checking for errors
            for key, value in errors.items():
                messages.error(request, value)
            return redirect ("/")
        User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST["email"],password=request.POST["password"],confirm_password=request.POST['confirmpw'])
        user = User.objects.get(email=request.POST['email'])
        request.session['user_id'] = user.id
        request.session['user_name'] = user.first_name
        request.session['first_name'] = user.first_name


    return redirect("/quotes")

def success(request): # render success page
    if 'user_name' in request.session:
        return render(request,"login_app/success.html")
    else:
        return redirect ("/")

def login(request): # login process
    if request.method == "POST":
        errors = User.objects.login_validator(request.POST)
        if len(errors): # checking for errors
            for key, value in errors.items():
                messages.error(request, value)
            return redirect ("/")
        else:
            user = User.objects.get(email=request.POST['login_email'])
            request.session['user_id'] = user.id #when user logged in, grabbed user ID
            request.session['user_name'] = user.first_name
            request.session['email'] = user.email
            request.session['first_name'] = user.first_name
            request.session['last_name'] = user.last_name
            request.session['password'] = user.password
            print(user.first_name)

        return redirect("/quotes")

def clear(request): # logout and clear sessions
    print("Clear session! and log out!")
    request.session.clear()
    return redirect('/')