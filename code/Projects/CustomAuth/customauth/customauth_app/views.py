from django.shortcuts import render, redirect
from customauth_app.forms import SignUpForm,SignInForm,UserProfileForm
from django.views.generic import View
from customauth_app.models import User,Profile
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.core.mail import send_mail
# Create your views here.

def send_otp(user_instance):
    user_instance.generate_otp()
    send_mail(
        "Verify otp",
        user_instance.otp,
        "manunmathew@gmail.com",
        [user_instance.email],
        fail_silently=False
    )

class SignUpView(View):
    def get(self, request, *args, **kwargs):
        form_instance=SignUpForm()
        return render (request, "register.html", {"form": form_instance})

    def post(self, request, *args, **kwargs):
        form_data = request.POST
        form_instance =SignUpForm(form_data)
        if form_instance.is_valid():
            user_instance = form_instance.save(commit=False)
            user_instance.is_active=False
            user_instance.save()
            send_otp(user_instance)
            return redirect("verifyotp")
        else:
            return render(request,"register.html",{"form":form_instance})

class VerifyOtpView(View):
    def get(self, request, *args, **kwargs):
        return render(request,"verify_otp.html")

    def post(self,request,*args, **kwargs):
        form_data=request.POST
        otp=form_data.get("otp")
        try:
            user_instance=User.objects.get(otp=otp)
            user_instance.is_active=True
            user_instance.is_verified=True
            user_instance.otp=None
            user_instance.save()
            return redirect("signin")
        except:
            messages.error(request,"Invalid Otp")
            return redirect("verifyotp")

class SignInView(View):
    def get(self, request, *args, **kwargs):
        form_instance = SignInForm()
        return render(request, "signin.html", {"form":form_instance})

    def post(self, request, *args, **kwargs):
        form_data = request.POST
        form_instance = SignInForm(form_data)
        if form_instance.is_valid():
            data=form_instance.cleaned_data
            uname = data.get("username")
            pwd = data.get("password")
            user_object = authenticate(request, username=uname,password=pwd)
            if user_object:
                login(request,user_object)
                return redirect("index")
        return render(request,"signin.html",{"form": form_instance})


class IndexView(View):
    def get(self, request, *args, **kwargs):

        return render(request, "index.html")

class ProfileUpdateView(View):
    def get(self, request, *args, **kwargs):
        profile_instance = request.user.userprofile
        form_instance =UserProfileForm(instance=profile_instance)
        return render(request, "profile_edit.html",{"form": form_instance})

    def post(self, request, *args, **kwargs):
        form_data=request.POST
        profile_instance=Profile.objects.get(owner=request.user)
        form_instance=UserProfileForm(form_data,instance=profile_instance,files=request.FILES)
        

