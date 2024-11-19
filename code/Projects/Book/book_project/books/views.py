from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import View
from .models import *
from .forms import *

# Create your views here.
class BookCreateView(View):
    def get(self, request, *args, **kwargs):
        form_instance = BookForm()
        return render(request, 'book_form.html', {'form': form_instance})

    def post(self, request, *args, **kwargs):
        form_instance = BookForm(request.POST)

        if form_instance.is_valid():
            data = form_instance.cleaned_data
            Book.objects.create(**data)
            return HttpResponse('Book added to the database')
        else:
            return HttpResponse('Failed to add the book')

class BookListView(View):
    def get(self, request):
        books = Book.objects.all()
        return render(request, 'book_list.html', {'books': books})


