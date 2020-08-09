# accounts models.py

from django.db import models
from django.contrib import auth

class Signup(models.Model):

    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
