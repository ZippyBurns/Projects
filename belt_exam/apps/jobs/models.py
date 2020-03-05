from __future__ import unicode_literals
from django.db import models
import bcrypt

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors={}
        if len(postData['fname']) < 2 :
            errors['fname'] = "You must provide a First Name"
        if len(postData['lname']) < 2 :
            errors['lname'] = "You must provide a Last Name"
        if len(postData['email']) < 1 :
            errors['email'] = "You must provide a valid e-mail"
        if len(postData['pword']) < 8 :
            errors['pword'] = "You must provide a password at least 8 characters long"
        return errors

    def login_validator(self, postData):
        errors={}
        results = User.objects.filter(email = postData['email'])
        if len(results) == 0 :
            errors['email'] = "Email address not found."
        elif not bcrypt.checkpw(postData['pword'].encode(), results[0].password.encode()):
            errors['password'] = "Password doesn't match"

        # else:
        #     errors['success'] = True
        return errors

    def form_validator(self, postData):
        errors={}
        if len(postData['title']) < 3:
            errors['title'] = "Title must be more then 3 characters"
        if len(postData['description']) < 10:
            errors['description'] = "Description must be 10 characters"
        if len(postData['location']) < 1:
            errors['location'] = "Location cannot be empty"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Job(models.Model):
    title = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    users = models.ManyToManyField(User, related_name="jobs")

class Userjob(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, related_name="userjobs")
