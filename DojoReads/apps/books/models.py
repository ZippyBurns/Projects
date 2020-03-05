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
            errors['email'] = "Login unsuccessful"
        elif not bcrypt.checkpw(postData['pword'].encode(), results[0].password.encode()):
            errors['password'] = "Login unsuccessful"
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    #ManytoMany w user.
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    #OneToMany w/ Rating
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Rating(models.Model):
    comment = models.CharField(max_length=255)
    rating = models.IntegerField(max_length=5)
    books = models.ForeignKey(Book, related_name="ratings")
    user = models.ManyToManyField(User, related_name="ratings")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
