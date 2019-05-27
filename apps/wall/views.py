######### FOR THE WALLLLLLL #########
from django.shortcuts import render, HttpResponse, redirect
from ..valid.models import User, Quote
from .models import *
from django.contrib import messages
from django.contrib.sessions.models import Session

def index(request):
    # if 'different' not in request.session:
    #     request.session['different'] = []
    if 'id' not in request.session:
        messages.success(request, "Not logged in!")
        return redirect('/')
    id = request.session['id']
    print('*' * 80)
    m = Message.objects.get(id=25)
    u = User.objects.get(id=id)
    print(m.likes_on_m.all())
    context = {
        "user": User.objects.get(id=id),
        "messages": Message.objects.order_by('-created_at'),
        "comments": Comments.objects.all(),
        "quotes" : Quote.objects.all()
    }
    # print(context)
    return render(request, "wall/show.html", context)

def create(request):
    id = request.session['id']
    if request.method == "POST":
        user = User.objects.get(id=id)
        mes = Message.objects.create(message=request.POST['message'], user=user)
        return redirect('/wall')

def create_comment(request, id):
    user = User.objects.get(id=request.session['id'])
    message_commented = Message.objects.get(id=id)
    if request.method == "POST":
        comment = Comments.objects.create(comment=request.POST['commentb'], messages=message_commented, user=user)
        print('*' * 80)
        print(request.POST)
        # print(comment.id)
        # print(comment.comment)
        # print(comment.user.first_name)
        # print(comment.messages.message)
    return redirect('/wall')

def likes(request, id):
    user_liking = User.objects.get(id=request.session['id'])
    being_liked = Message.objects.get(id=id)
    being_liked.likes_on_m.add(user_liking)
    being_liked.save()
    return redirect('/wall')

def unlikes(request, id):
    user_unliking = User.objects.get(id=request.session['id'])
    being_unliked = Message.objects.get(id=id)
    being_unliked.likes_on_m.remove(user_unliking)
    return redirect('/wall')

def destroy(request, id):
    c_destroy = Comments.objects.get(id=id)
    c_destroy.delete()
    return redirect('/wall')

def destroym(request, id):
    m_destroy = Message.objects.get(id=id)
    m_destroy.delete()
    return redirect('/wall')