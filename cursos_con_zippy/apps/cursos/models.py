from __future__ import unicode_literals
from django.db import models
import bcrypt

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors={}
        if len(postData['fname']) < 2 :
            errors['fname'] = "You must provide a First Name // Debes proveer un nombre válido"
        if len(postData['lname']) < 2 :
            errors['lname'] = "You must provide a Last Name // Debes proveer un apellido válido"
        if len(postData['email']) < 1 :
            errors['email'] = "You must provide a valid e-mail // Debes proveer un correo electronico válido"
        if len(postData['pword']) < 8 :
            errors['pword'] = "You must provide a password at least 8 characters long // la contraseña tuya debe tener 8 caractares"
        return errors

    def login_validator(self, postData):
        errors={}
        results = User.objects.filter(email = postData['email'])
        if len(results) == 0 :
            errors['email'] = "Login unsuccessful / inicio de sesiòn fallido"
        elif not bcrypt.checkpw(postData['pword'].encode("utf-8"), results[0].password.encode()):
            errors['password'] = "Login unsuccessful / inicio de sesiòn fallido"
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()


class Message(models.Model):
    message = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    # user = models.ForeignKey(User, related_name="messages")


class Comment(models.Model):
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # message= models.ForeignKey(Message, related_name="comments")
    # user = models.ForeignKey(User, related_name="comments")

