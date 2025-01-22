from django.shortcuts import redirect
from django.contrib import messages

def signin_required(fn):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            messages.error(request,"Invalid session")
            return redirect("signin")
        else:
            return fn(request,*args,**kwargs)
    return wrapper
