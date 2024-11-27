from django.shortcuts import render,redirect
from django.views.generic import View
from expense.forms import ExpenseCreateForm
from expense.models import Transaction

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
            form_instance.save()
            return redirect("expenselist")

class ExpenseListView(View):
    template_name = "expense_list.html"
    def get(self, request, *args, **kwargs):
        qs = Transaction.objects.all()
        return render(request, self.template_name, {"data" : qs} )

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
    def post(self, request, *args, **kwargs):
        form_instance = self.form_class(request.POST)
        id = kwargs.get("pk")

        if form_instance.is_valid():
            data=form_instance.cleaned_data
            Transaction.objects.filter(id=id).update(**data)
            return redirect("expenselist")
        return render(request, self.template_name, {"form": form_instance})
