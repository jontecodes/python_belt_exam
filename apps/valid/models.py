######### FOR VAAAALLLIIDDDDD #########
from __future__ import unicode_literals
from django.db import models
from django.core.exceptions import ObjectDoesNotExist
import re
from datetime import datetime
date = datetime.now()
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        context = {
            "user": User.objects.all()
        }
        grab = User.objects.filter(email=postData['email'])
        print(grab)
        print('*' * 80)
        if len(postData['fn']) < 2:
            errors['fn'] = "First Name should be more than 2 characters"
            print(grab)
        if len(postData['ln']) < 2:
            errors['ln'] = "Last name should be more than 2 characters"
        if not EMAIL_REGEX.match(postData["email"]):
            errors['email'] = "Email not entered in valid form"
        if len(grab) > 0:
            errors['email'] = "Email already exists"
        if len(postData['password']) < 8:
            errors['password'] = "Password should be at least 8 characters"
        if postData['password'] != postData['password_confirm']:
            errors['password_confirm'] = "Passwords do not match!"
        return errors

    def edit_validator(self, postData):
        errors = {}
        if len(postData['fnn']) < 1:
            errors['fnn'] = "You must change your first name to at least 1 character."
        if len(postData['lnn']) < 1:
            errors['lnn'] = "You must change your last name to at least 1 character."
        if not EMAIL_REGEX.match(postData["em"]):
            errors['em'] = "Email not entered in valid form"
        return errors

    def login_validator(self, postData):
        errors = {}
        context = {
            "users": User.objects.all()
        }
        email = User.objects.filter(email=postData['email'])
        print(email)
        if len(email) == 0:
            errors["emaillog"] = "Email is not registered"
        else:
            user = User.objects.get(email=postData['email'])
            if user.password != postData['password']:
                errors['pwlog'] = "Password does not match"
        return errors


class QuoteManager(models.Manager):

    def quote_validator(self, postData):
        errors = {}

        if len(postData['author']) < 4:
            errors['author'] = "Author name should be at 4 characters long."

        if len(postData['quote']) < 11:
            errors['quote'] = "Quote should be at least 11 characters long."

        return errors





class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()
    def __repr__(self):
        return f"<Shows object: {self.id} ({self.email})>"

class Quote(models.Model):
    quote = models.TextField()
    author = models.CharField(max_length=255)
    user = models.ForeignKey(User, related_name="quotes")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes_on_quotes = models.ManyToManyField(User, related_name="quotes_user_liked")
    objects = QuoteManager()

    def __repr__(self):
        return f"<Quote object: {self.id} Author:({self.author})>"
