from django.shortcuts import render,redirect
from django.views.generic import View
from expense.forms import ExpenseCreateForm
from expense.models import Transaction
from django.db.models import Sum
from .forms import SignUpForm,LoginForm


# Create your views here.

class ExpenseCreateView(View):
    template_name = "expense_add.html"
    form_class = ExpenseCreateForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})
    def post(self, request, *args, **kwargs):
        form_instance = self.form_class(request.POST)
        if form_instance.is_valid():
            # data = form_instance.cleaned_data
            # Transaction.objects.create(**data)
            form_instance.instance.owner=request.user
            form_instance.save()
            return redirect("expenselist")

class ExpenseListView(View):
    template_name = "expense_list.html"
    def get(self, request, *args, **kwargs):
        qs = Transaction.objects.all()
        selected_category = request.GET.get("category")
        if selected_category:
            qs = qs.filter(category = selected_category)
        categories = Transaction.objects.all().values_list('category', flat=True).distinct()

        return render(request, self.template_name, {"data" : qs, "categories" : categories } )

class ExpenseDetailView(View):
    template_name = "expense_detail.html"
    def get(self,request, *args, **kwargs):
        id = kwargs.get("pk")
        qs = Transaction.objects.get(id=id)
        return render(request, self.template_name, {"data" : qs} )

class ExpenseRemoveView(View):
    def get(self,request, *args, **kwargs):
        id = kwargs.get("pk")
        Transaction.objects.get(id=id).delete()
        return redirect("expenselist")


class ExpenseUpdateView(View):
    template_name = "expense_update.html"
    form_class = ExpenseCreateForm

    def get(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        instance =Transaction.objects.get(id=id)
        instance_dict = {
            "title": instance.title,
            "amount": instance.amount,
            "category": instance.category,
            "payment_method": instance.payment_method,
            "priority": instance.priority
        }
        form_instance = self.form_class(initial= instance_dict)
        return render(request, self.template_name, {"form": form_instance})
    # def post(self, request, *args, **kwargs):
    #     form_instance = self.form_class(request.POST)
    #     id = kwargs.get("pk")

    #     if form_instance.is_valid():
    #         data=form_instance.cleaned_data
    #         Transaction.objects.filter(id=id).update(**data)
    #         return redirect("expenselist")
    #     return render(request, self.template_name, {"form": form_instance})
    def post (self, request, *args, **kwargs) :
        id=kwargs.get("pk")
        transaction_object=Transaction.objects.get(id=id)
        form_instance=self.form_class(request.POST, instance=transaction_object)
        if form_instance.is_valid():
            form_instance. save()#update
            return redirect("expenselist")
        return render (request, self. template_name, {"form": form_instance})
class ExpenceSummaryView(View):
    template_name = "expense_summary.html"
    form_class = ExpenseCreateForm
    def get(self, request, *args, **kwargs):
        total_expense = Transaction.objects.all().aggregate(total = Sum("amount"))
        category_summary = Transaction.objects.all().values("category").annotate(total = Sum("amount"))
        paymethod_summary = Transaction.objects.all().values("payment_method").annotate(total = Sum("amount"))
        priority_summary = Transaction.objects.all().values("priority").annotate(total = Sum("amount"))
        context = {
            "expense_total": total_expense.get("total"),
            "category_total": category_summary,
            "paymethod_total": paymethod_summary,
            "priority_total": priority_summary
        }
        return render(request, self.template_name, context)


class SignUpView(View):
    template_name = "register.html"
    form_class = SignUpForm

    def get(self, request, *args, **kwargs):
        # Display the empty form on GET request
        form_instance = self.form_class()
        return render(request, self.template_name, {"form": form_instance})

    def post(self, request, *args, **kwargs):
        # Handle form submission on POST request
        form_instance = self.form_class(request.POST)
        if form_instance.is_valid():
            # Retrieve cleaned data from the form
            data = form_instance.cleaned_data
            # Create a new user
            User.objects.create_user(
                username=data['username'],
                email=data['email'],
                password=data['password1']  # Use password1 (validated by UserCreationForm)
            )
            return redirect("login")  # Redirect to the login page or any desired page
        # If the form is not valid, re-render the form with errors
        return render(request, self.template_name, {"form": form_instance})


class SignUpView(View):
    template_name = "register.html"  # Path to your HTML template
    form_class = SignUpForm  # Assign the form class

    def get(self, request, *args, **kwargs):
        # Display an empty form on GET request
        form_instance = self.form_class()
        return render(request, self.template_name, {"form": form_instance})

    def post(self, request, *args, **kwargs):
        # Handle form submission on POST request
        form_instance = self.form_class(request.POST)
        if form_instance.is_valid():
            form_instance.save()  # Save the new user to the database
            return redirect("login")  # Redirect to login page after successful registration
        # If the form is invalid, re-render the form with errors
        return render(request, self.template_name, {"form": form_instance})


class SignInView(View):
    template_name = "sign_in.html"
    form_class = LoginForm
    def get(self, request,*args,**kwargs):
        form_instance = self.form_class()

