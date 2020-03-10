from django.shortcuts import render, redirect, HttpResponse
import bcrypt
from .models import User, Message, Comment
from django.contrib import messages

def index(request):           
    if request.method == "GET":
        context = {"user" : User.objects.all()}
        return render(request, 'index.html', context)
    if request.method == "POST":  
        errors = User.objects.basic_validator(request.POST)
        if len(errors) > 0:
        # check if the dictionary contains any errors
        #if there are errors...
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            pw_hash = bcrypt.hashpw(request.POST["pword"].encode("utf-8"), bcrypt.gensalt())
            print("password hash: ", pw_hash)
            new_user = User.objects.create(first_name=request.POST['fname'],last_name=request.POST['lname'], email=request.POST['email'], password=pw_hash)
            print("New user: ", new_user.id)
            request.session['id'] = new_user.id
            return redirect("/home")

def username(request):
    if request.method == "POST":
        context = {
            "found" : False
        }
        res = User.objects.filter(email =request.GET.get('email', ""))
        if len(res) > 0:
            context['found'] = True
            #ajax email verificar
        return render(request, "username.html", context)

def homepage(request):
    if 'id' not in request.session:
        return redirect("/")
    else:   
        if request.method == 'GET':
            print("/home get in function")
            # all_cursos = Hotspring.objects.all().order_by("-updated_at")
            user = User.objects.get(id=request.session['id'])
            print(user)
            print("session id: ", request.session['id'])
            context = {
                "user" : user,
                }
            return render (request, 'home.html', context)

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
            return redirect ("/home")
            
def library(request):
    if 'id' not in request.session:
        return redirect("/")
    if request.method == "GET":
        user = User.objects.get(id=request.session['id'])
        context = {
            "user" : user,
        }
        return render(request, 'library.html', context)

def logout(request):
    if 'id' not in request.session:
        return redirect("/")
    request.session.clear()
    return redirect ("/home")

def greeting(request):
    if 'id' not in request.session:
        return redirect("/")
    if request.method == "GET":
        user = User.objects.get(id=request.session['id'])
        context = {
            "user" : user,
        }
        return render(request, 'greeting.html', context)

def color(request):
    if 'id' not in request.session:
        return redirect("/")
    if request.method == "GET":
        user = User.objects.get(id=request.session['id'])
        context = {
            "user" : user,
        }
        return render(request, 'color.html', context)

def number(request):
    if 'id' not in request.session:
        return redirect("/")
    if request.method == "GET":
        user = User.objects.get(id=request.session['id'])
        context = {
            "user" : user,
        }
        return render(request, 'number.html', context)
        
