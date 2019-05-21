from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages


def index(request):
    context = {
        "users": User.objects.all()
    }
    users = User.objects.all()
    print(users)
    return render(request, "valid/index.html")

def create(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    if request.method == "POST":
        user = User.objects.create(first_name=request.POST['fn'], last_name=request.POST['ln'], email=request.POST['email'], password=request.POST['password'])
        messages.success(request, "Successfully registered!")
        request.session['id'] = user.id
        print(request.session['id'])
        return redirect('/show')

def show(request):
    if 'id' not in request.session:
        messages.success(request, "Not logged in!")
        return redirect('/')
    id = request.session['id']
    context = {
        "user": User.objects.get(id=id)
    }
    return render(request, "valid/show.html", context)

def login(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    if request.method == "POST":
        user = User.objects.get(email=request.POST['email'])
        print(user.id)
        request.session['id'] = user.id
        messages.success(request, "Successfully Logged in!")
        return redirect("/show")

def logout(request):
    request.session.clear()
    return redirect('/')
