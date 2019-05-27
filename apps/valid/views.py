######### FOR VAAAALLLIIDDDDD #########
from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages

## This is Ricardos Login/Reg code##


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
        return redirect('/quotes')


def show(request):
    return redirect("/wall")


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
        return redirect("/quotes")


def logout(request):
    request.session.clear()
    return redirect('/')

## This is my code for the exam##


def quotes(request):
    user = request.session['id']
    
    
    
    context = {
        'quotes': Quote.objects.all(),
        'user': User.objects.get(id=user)

    }
    return render(request, 'valid/quotes.html', context)


def add_quote(request):

    errors = Quote.objects.quote_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/quotes')
    if request.method == 'POST':
        Quote.objects.create(quote=request.POST['quote'], author=request.POST['author'], user=User.objects.get(
            id=request.session['id']))

    return redirect('/quotes')


def del_quote(request):
    deleted_quote = Quote.objects.get(id=request.POST
    ['quote-id'])
    deleted_quote.delete()
    return redirect('/quotes')

def user_quotes(request, quote_id):

    context = {
        'quotes': Quote.objects.filter(user = quote_id),
        'user': User.objects.get(id=quote_id)

    }
    print(context)
    print('%' * 20)
    return render(request, 'valid/user-quote.html', context)

def edit_user(request, acc_id):
    id = request.session['id']
    context = {
        'user' : User.objects.get(id=id)
    }
    return render(request, 'valid/edit.html', context)

def update_user(request):
    id = request.session['id']
    errors = User.objects.edit_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/myaccount/{id}')
    if request.method == 'POST':
        user = User.objects.get(id=request.session['id'])
        user.first_name = request.POST['fnn']
        user.last_name = request.POST['lnn']
        user.email = request.POST['em']
        user.save()
    return redirect('/quotes')

def like_quote(request, q_id ):
    this_user = User.objects.get(id=request.session['id'])
    quote = Quote.objects.get(id=q_id)
    quote.likes_on_quotes.add(this_user)
    quote.save()

    return redirect('/quotes')

