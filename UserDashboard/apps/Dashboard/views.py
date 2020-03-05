from django.shortcuts import render

from django.shortcuts import render, redirect, HttpResponse
import bcrypt
from .models import User, Message, Comment
from django.contrib import messages 

# *** ** Start Authenication **** *** **
def index(request):           
    if request.method == "GET":
        return render(request, 'Dashboard/index.html', {"user" : User.objects.all()})
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
            return redirect("/success")

def username(request):
    # if request.method == "POST":
        context = {
            "found" : False
        }
        res = User.objects.filter(email =request.GET.get('email', ""))
        if len(res) > 0:
            context['found'] = True

        return render(request, "Dashboard/username.html", context)


def success(request):
    if 'id' not in request.session:
        return redirect("/")
    else:   
        if request.method == 'GET':
            current_user = User.objects.get(id=request.session['id'])
            context ={
                "user" : current_user
            }
            return render (request, 'Dashboard/success.html', context)


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
            return redirect ("/success")

def logout(request):
    request.session.clear()
    return redirect ("/")
#  *** *** * End of Authentication ****** * * * * * *

# ***** adiminstrator functions *******
def admin (request):
    if request.method == 'GET':
            all_users = User.objects.all()
            current_user = User.objects.get(id=request.session['id'])
            context={
                "current_user" : current_user,
                "all_users" : all_users,
            }
    return render (request, "Dashboard/adminDashboard.html", context)

def adduser(request):
    return render(request, "Dashboard/adminAdd.html")
#   **** END ADMIN FUNCTIONS ****** 

# **** Profile and Messaging functions *****
def profile(request, my_val):
    if 'id' not in request.session:
        return redirect("/")
    else:
        if request.method == 'GET':
            user_profile = User.objects.get(id=my_val)
            current_user = User.objects.get(id=request.session['id'])
            all_messages = Message.objects.all()
            all_comments = Comment.objects.all()

            context={
                "current_user" : current_user,
                "user_profile" : user_profile,
                "all_comments" : all_comments,
                "all_messages" : all_messages,                
            }
    return render(request, "Dashboard/profile.html", context)
def send_message(request, my_val):
    if request.method == "POST":
        print(request.session['id'])
        user = User.objects.get(id = request.session['id'])
        new_message = Message.objects.create(message=request.POST['message'], user = user,)
        print(new_message, "**********************")
        return redirect("/profile/"+ my_val)

def send_comment(request, my_val):
    if request.method == "POST":
        user = User.objects.get(id = request.session['id'])
        message = Message.objects.get(id = request.POST['message_id'] )
        comment = Comment.objects.create(comment=request.POST['comment'], user = user, message=message)
        my_val = my_val
        print(message.comments,"***********************")
        return redirect("/profile/" + my_val)

def delete_message(request, my_val):
    delete = Message.objects.get(id = my_val)
    delete.delete()
    return redirect("/profile/" + my_val)

def delete_comment(request, my_val):
    delete = Comment.objects.get(id = my_val)
    delete.delete()
    return redirect("/profile/" + my_val)

#  *** END PROFILE AND SOCIAL FUNCTIONS ***