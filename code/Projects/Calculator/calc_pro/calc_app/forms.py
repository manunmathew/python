from django import forms


class FilmForm(forms.Form):
    films_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Enter Film Name'}))
    release_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    director = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder': 'Enter Director Name'}))
