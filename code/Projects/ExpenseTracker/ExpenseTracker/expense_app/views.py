from django.shortcuts import render,redirect
from django.views.generic import View
from expense_app.forms import SignUpForm,SignInForm,ExpenseForm
from expense_app.models import Expense
from django.contrib.auth import authenticate,login,logout
from django.db.models import Sum,Count
from expense_app.decorators import signin_required
from django.utils.decorators import method_decorator
from django.contrib import messages
# Create your views here.


class SignUpView(View):
    template_name = "register.html"
    def get(self,request,*args,**kwargs):
        form_instance = SignUpForm()
        return render(request, self.template_name, {"form": form_instance})

    def post(self,request,*args,**kwargs):
        form_data=request.POST
        form_instance=SignUpForm(form_data)
        if form_instance.is_valid():
            form_instance.save()
            print("-----Account Created-------")
            messages.success(request, "Account Created")
            return redirect("register")
        else:
            print("-----Account Creation Failed-------")
            messages.error(request, "Account Account Creation Failed")
            return render(request, self.template_name, {"form": form_instance})

class SignInView(View):

    def get(self,request,*args,**kwargs):
        form_instance=SignInForm()
        return render(request,"signin.html",{"form":form_instance})
    def post(self,request,*args,**kwargs):
        form_data=request.POST
        form_instance=SignInForm(form_data)
        if form_instance.is_valid():
            data=form_instance.cleaned_data
            uname=data.get("username")
            pwd=data.get("password")
            user_instance=authenticate(request,username=uname,password=pwd)
            if user_instance:
                login(request,user_instance)
                print("------Success-----")
                return redirect("index")
            else:
                print("------Login failed-----")
                return render(request,"signin.html",{"form":form_instance})

@method_decorator(signin_required, name="dispatch")
class IndexView(View):
    def get(self,request,*args,**kwargs):
        total_expense = Expense.objects.filter(owner=request.user).values('amount').aggregate(total=Sum("amount"))
        category_summary = Expense.objects.filter(owner=request.user).values('category').annotate(total=Sum("amount"),count=Count('category')).order_by("-total")
        print(category_summary)
        context ={
            "total_expense":total_expense.get("total"),
            "category_summary":category_summary
        }
        return render(request,"index.html", context)

@method_decorator(signin_required, name="dispatch")
class SignOutView(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("signin")

@method_decorator(signin_required, name="dispatch")
class ExpenseCreateView(View):
    def get(self,request,*args,**kwargs):
        form_instance = ExpenseForm()
        qs = Expense.objects.filter(owner=request.user).order_by("-created_at")
        return render(request,"expense_add.html",{"form": form_instance, "data": qs})
    def post(self,request,*args,**kwargs):
        form_data=request.POST
        form_instance=ExpenseForm(form_data)
        if form_instance.is_valid():
            #data=form_instance.cleaned_data
            # Expense.objects.create(**data,owner=request.user)

            form_instance.instance.owner = request.user
            form_instance.save()
            return redirect("expenseadd")
        else:
            return render(request,"signin.html", {"form": form_instance})

@method_decorator(signin_required, name="dispatch")
class ExpenseDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Expense.objects.get(id=id).delete()
        return redirect("expenseadd")

@method_decorator(signin_required, name="dispatch")
class ExpenseUpdateView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        expense_object=Expense.objects.get(id=id)
        form_instance=ExpenseForm(instance=expense_object)
        return render(request, "expense_edit.html", {'form':form_instance})

    def post(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        expense_object=Expense.objects.get(id=id)
        form_data =request.POST
        form_instance=ExpenseForm(form_data, instance=expense_object)
        if form_instance.is_valid():
            form_instance.save()
            return redirect("expenseadd")
        else:
            return render(request, "expense_edit.html", {'form':form_instance})

