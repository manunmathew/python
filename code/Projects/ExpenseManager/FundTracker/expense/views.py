from django.shortcuts import render
from django.views.generic import View
from expense.forms import ExpenseCreateForm

# Create your views here.

class ExpenseCreateView(View):
    template_name = "expense_add.html"
    form_class = ExpenseCreateForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

