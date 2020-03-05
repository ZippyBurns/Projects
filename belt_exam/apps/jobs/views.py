from django.shortcuts import render, redirect, HttpResponse
import bcrypt
from .models import User, Job, Userjob
from django.contrib import messages

def index(request):           
    if request.method == "GET":
        return render(request, 'jobs/index.html', {"user" : User.objects.all()})
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
            return redirect("/dashboard")

def dashboard(request):
    if 'id' not in request.session:
        return redirect("/")
    else:   
        if request.method == 'GET':
            current_user = User.objects.get(id=request.session['id'])
            all_jobs = Job.objects.all()
            context ={
                "user" : current_user,
                "all_jobs" : all_jobs
            }
            return render (request, 'jobs/dashboard.html', context)

def addJob(request):
    if request.method == 'GET':
        all_jobs = Job.objects.all()
        current_user = User.objects.get(id=request.session['id'])
        context={
            "user" : current_user,
            "all_jobs" : all_jobs
        }
        return render (request, 'jobs/addJob.html', context)
    if request.method == 'POST':
        errors = User.objects.form_validator(request.POST)
        if len(errors) > 0:
        #check if the dictionary contains any errors
        #if there are errors...
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/addJob')
        else:
            new_job = Job.objects.create(title=request.POST['title'], description=request.POST['description'],location=request.POST['location'])
            return redirect ('/dashboard')

def addlist(request, id):
    if request.method == 'POST':
        job = Job.objects.get(id=id)
        user_list = Userjob.objects.create(title= job)

def view(request, id):
    current_job = Job.objects.get(id = id)
    context ={
        "job" : current_job
    }
    return render(request, 'jobs/viewjobs.html', context)

def edit(request, id):
    if request.method == "GET":
        current_job = Job.objects.get(id = id)
        context ={
        "job" : current_job
    }
        return render(request, 'jobs/editjobs.html', context)
    if request.method == "POST":
        errors = User.objects.form_validator(request.POST)
        if len(errors) > 0:
        #check if the dictionary contains any errors
        #if there are errors...
            for key, value in errors.items():
                messages.error(request, value)
            return redirect("/edit/"+str(id))
        else:
            edit = Job.objects.get(id=id)
            edit.title = request.POST['title']
            edit.description = request.POST['description']
            edit.location = request.POST['location']
            edit.save()
    return redirect("/view/"+str(id))

def delete(request, id):
    delete = Job.objects.get(id = id)
    delete.delete()
    return redirect("/dashboard")

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
            return redirect ("/dashboard")

def logout(request):
    request.session.clear()
    return redirect ("/")




