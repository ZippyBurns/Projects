from django.shortcuts import render, redirect, HttpResponse
import bcrypt
from .models import *
from django.contrib import messages

from django.shortcuts import render, redirect, HttpResponse
import bcrypt
from .models import User
from django.contrib import messages

def index(request):           
    if request.method == "GET":
        return render(request, 'wall/index.html', {"user" : User.objects.all()})
    if request.method == "POST":
        
        errors = User.objects.basic_validator(request.POST)
        if len(errors) > 0:
        #check if the dictionary contains any errors
        #if there are errors...
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            pw_hash = bcrypt.hashpw(request.POST["pword"].encode(), bcrypt.gensalt())
            new_user = User.objects.create(first_name=request.POST['fname'],last_name=request.POST['lname'], email=request.POST['email'], password=pw_hash)
            request.session['id'] = new_user.id
            return redirect("/wall")

def wall(request):
    if 'id' not in request.session:
        return redirect("/")
    else:   
        if request.method == 'GET':
            all_users = User.objects.all()
            all_messages = Message.objects.all()
            all_comments = Comment.objects.all()
            current_user = User.objects.get(id=request.session['id'])
            context ={
                "current_user" : current_user,
                "all_messages" : all_messages,
                "all_users" : all_users,
                "all_comments" : all_comments
            }
            return render (request, 'wall/wall.html', context)

def login(request):
    if request.method == "POST":
        errors = User.objects.login_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            user = User.objects.get(email=request.POST['email'])
            request.session['id'] = user.id
            return redirect ("/wall")

def send_message(request):
    if request.method == "POST":
        print(request.session['id'])
        user = User.objects.get(id = request.session['id'])
        new_message = Message.objects.create(message=request.POST['message'], user = user,)
        return redirect("/wall")

def send_comment(request):
        if request.method == "POST":
            
            user = User.objects.get(id = request.session['id'])
            message = Message.objects.get(id = request.POST['message_id'] )
            comment = Comment.objects.create(comment=request.POST['comment'], user = user, message=message)
            print(message.comments,"***********************")

            return redirect("/wall")

def delete_message(request, id):
    delete = Message.objects.get(id = id)
    delete.delete()
    return redirect("/wall")

def delete_comment(request, id):
    delete = Comment.objects.get(id = id)
    delete.delete()
    return redirect("/wall")

def logout(request):
    request.session.clear()
    return redirect ("/")