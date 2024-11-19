from django import forms


class BookForm(forms.Form):
    title = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'placeholder': 'Enter Book Title'}))
    author = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'placeholder': 'Enter Author Name'}))
    pages = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Enter Number of Pages'}))
    published_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
