from django import forms
from expense.models import Transaction

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

# class ExpenseCreateForm(forms.ModelForm):
#     class Meta:
#         model = Transaction
#         fields =["title","amount","category","payment_method","priority"]

