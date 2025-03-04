from django import forms
from django.contrib.auth.forms import UserCreationForm
from customauth_app.models import User,Profile

class SignUpForm(UserCreationForm):
    class Meta:
        model=User
        fields=["username", "email", "password1", "password2", "phone" ]

class SignInForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

class UserProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        exclude=('owner',)
