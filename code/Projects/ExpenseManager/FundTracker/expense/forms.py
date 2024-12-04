from django import forms
from expense.models import Transaction
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# class ExpenseCreateForm(forms.Form):
#     title = forms.CharField()
#     amount = forms.FloatField()
#     category = forms.ChoiceField(choices=Transaction.CATEGORY_OPTIONS)
#     payment_method = forms.ChoiceField(choices=Transaction.PAYMENT_OPTIONS)
#     priority = forms.ChoiceField(choices=Transaction.PRIORITY_OPTIONS)

class ExpenseCreateForm(forms.ModelForm):
    class Meta:
        model = Transaction
        exclude = ("created_date",)
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control mt-2"}),
            "amount": forms.NumberInput(attrs={"class": "form-control mt-2"}),
            "category":forms.Select(attrs={"class": "form-control form-select mt-2"}),
            "payment_method":forms.Select(attrs={"class": "form-control form-select mt-2"}),
            "priority":forms.Select(attrs={"class": "form-control form-select mt-2"})
        }

# class ExpenseCreateForm(forms.ModelForm):
#     class Meta:
#         model = Transaction
#         fields =["title","amount","category","payment_method","priority"]


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User  # Use the default Django User model
        fields = ['username', 'email', 'password']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

