Auth application

django.contrib.auth

Model

class AbstractBaseUser(models.Model):
    password=model.CharField()


class AbstractUser(AbstractBaseUser):
    username
    first_name
    last_name
    email

class User(AbstractUser)


Forms

forms.py

from django import forms
from django.contrib.auth.models import User

class SignUpForm(forms.ModelForm):
    class Meta:
        
