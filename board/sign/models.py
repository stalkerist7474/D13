from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.models import User
from django.db import models


class User(models.Model):
    full_name = models.CharField(max_length = 255)
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    #alluath основа
    def __str__(self):
        return f'{self.full_name.title()}'