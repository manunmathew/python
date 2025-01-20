from django.shortcuts import render,redirect

from django.views.generic import View

from store.forms import BookForm
from store.models import Book
from django.db.models import Q

# Create your views here.


# BookCreateView
# url:localhost:8000/books/add/
# method:

    # GET:book_add.html,form
    #POST:create  book object


class BookCreateView(View):

    def get(self,request,*args,**kwargs):

        form_instance=BookForm()

        return render(request,"book_add.html",{"form":form_instance})

    def post(self, request, *args, **kwargs):
        form_data=request.POST

        form_instance=BookForm(form_data, files=request.FILES)
        if form_instance.is_valid():
            data=form_instance.cleaned_data
            Book.objects.create(**data)
            return redirect("book-list")
        return render(request,"book_add.html",{"form":form_instance})

class BookListView(View):
    def get(self,request, *args, **kwargs):
        search_text=request.GET.get("search")
        qs=Book.objects.all()
        if search_text:
            qs=qs.filter(Q(title__contains=search_text)|Q(author__contains=search_text))
        return render(request, "book_list.html", {"data": qs})




class BookDeleteView(View):
    def get(self,request,*args,**kwargs):
        id = kwargs.get("pk")
        Book.object.get(id=id).delete()
        return redirect("book-list")


class BookUpdateView(View):
    def get(self,request,*args,**kwargs):
        id = kwargs.get("id")
        book_obj=Book.object.get.get(id=id)
        book_dictionary = {
            "title":book_obj.title,
            "author":book_obj.author,
            "price":book_obj.price,
            "language":book_obj.language,
            "genre":book_obj.genre,
            "year":book_obj.genre
        }
        form_instance = BookForm(initial=book_dictionary)
        return render(request,"book_edit.html",{"form":form_instance})

    def post(self,request,*args,**kwargs):
        form_data=request.POST
        form_instance=BookForm(form_data)
        id = kwargs.get("pk")
        if form_instance.is_valid():
            data = form_instance.cleaned_data
            Book.object.filter(id=id).update(**data)
            return redirect("book-list")
        return render(request,"book_edit.html",{"form":form_instance})
