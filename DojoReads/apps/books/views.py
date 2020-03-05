from django.shortcuts import render, redirect, HttpResponse
import bcrypt
from .models import User, Book, Rating
from django.contrib import messages
# *** ** Start Authenication **** *** **
def index(request):           
    if request.method == "GET":
        return render(request, 'books/index.html', {"user" : User.objects.all()})
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
            return redirect("/homepage")

def username(request):
    # if request.method == "POST":
        context = {
            "found" : False
        }
        res = User.objects.filter(email =request.GET.get('email', ""))
        if len(res) > 0:
            context['found'] = True

        return render(request, "books/username.html", context)


def homepage(request):
    if 'id' not in request.session:
        return redirect("/")
    else:   
        if request.method == 'GET':
            current_user = User.objects.get(id=request.session['id'])
            recent_ratings = User.objects.all().order_by("-updated_at") 
            context ={
                "current_user" : current_user,
                "recent_ratings" : recent_ratings
            }
            return render (request, 'books/homepage.html', context)


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
            return redirect ("/homepage")

def logout(request):
    request.session.clear()
    return redirect ("/")
#  *** *** * End of Authentication ****** * * * * * *

def addbook(request):
    return render(request, "books/addBook.html")

def viewbook(request, my_val):
    if request.method == 'GET':
        current_user = User.objects.get(id=request.session['id'])
        book = Book.objects.get(id = my_val)
        all_ratings = Rating.objects.all()
        context={
            "my_val":my_val,
            "current_user" : current_user,
            "book" : book,
            "all_ratings" : all_ratings,
    }
    return render(request, "books/viewBook.html")