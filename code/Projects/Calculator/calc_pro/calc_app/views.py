from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import View
from .models import *
from .forms import *
# Create your views here.

# HttpResponse
# Its a function that is used to generate a text response in django
# View
# a function that handles the http requests and response that includes get() post() put() delete()

class First(View):
    def get(self, request):
        return HttpResponse("Welcome to django")

class Second(View):
    def get(self, request):
        return HttpResponse("Django Njan pettu")

class Template1(View):
    def get(self, request):
        return render(request, "first.html")

class Index(View):
    def get(self, request):
        return render(request, "index.html")

class Addition(View):
    def get(self, request):
        return render(request, "add.html")
    def post(self,request):
        n1 = int(request.POST.get('first_number'))
        n2 = int(request.POST.get('second_number'))
        ans =n1 + n2

        Add_model.objects.create(num1=n1, num2=n2, Answer=ans)
        return render(request, 'add.html', {'Answer':ans, 'N1': n1, 'N2': n2})



class Subtraction(View):
    def get(self, request):
        return render(request, "sub.html")

    def post(self,request):
        n1 = int(request.POST.get('first_number'))
        n2 = int(request.POST.get('second_number'))
        ans =n1 - n2

        Sub_model.objects.create(num1=n1, num2=n2, Answer=ans)
        return render(request, 'sub.html', {'Answer':ans, 'N1': n1, 'N2': n2})

class Multiplication(View):
    def get(self, request):
        return render(request, "multiply.html")
    def post(self,request):
        n1 = int(request.POST.get('first_number'))
        n2 = int(request.POST.get('second_number'))
        ans =n1 * n2

        Multi_model.objects.create(num1=n1, num2=n2, Answer=ans)
        return render(request, 'multiply.html', {'Answer':ans, 'N1': n1, 'N2': n2})

class Division(View):
    def get(self, request):
        return render(request, "div.html")
    def post(self,request):
        n1 = int(request.POST.get('first_number'))
        n2 = int(request.POST.get('second_number'))
        ans =n1 / n2

        Div_model.objects.create(num1=n1, num2=n2, Answer=ans)
        return render(request, 'div.html', {'Answer':ans, 'N1': n1, 'N2': n2})
class AreaOfCircle(View):
    def get(self, request):
        return render(request, "circle.html")

    def post(self, request):
        radius = float(request.POST.get('radius'))
        area = 3.14159 * radius * radius

        CircleArea_model.objects.create(radius=radius, area=area)
        return render(request, 'circle.html', {'CircleArea': area, 'Radius': radius})

class AreaOfTriangle(View):
    def get(self, request):
        return render(request, "triangle.html")

    def post(self, request):
        base = float(request.POST.get('base'))
        height = float(request.POST.get('height'))
        area = 0.5 * base * height

        TriangleArea_model.objects.create(base=base, height=height, area=area)
        return render(request, 'triangle.html', {'TriangleArea': area, 'Base': base, 'Height': height})

class Add_display_view(View):
    def get(self, request):
        data=Add_model.objects.all()
        return render(request, 'addview.html', {'data': data})


class Sub_display_view(View):
    def get(self, request):
        data=Sub_model.objects.all()
        return render(request, 'subview.html', {'data': data})

class Add_delete_view(View):
    def get(self, request, *args, **kwargs):
        id=kwargs.get('id')
        Add_model.objects.get(id=id).delete()
        return redirect('/addview/')


class film_create(View):
    def get(self, request, *args, **kwargs):
        form_instance=FilmForm()
        return render(request, 'film.html', {'form': form_instance})
    def post(self, request):
        form_instance=FilmForm(request.POST)

        if form_instance.is_valid():
            data=form_instance.cleaned_data
            FilmCreateModel.objects.create(**data)
            return HttpResponse('Film added to database')
        else:
            return HttpResponse('Failed')

class display_film(View):
    def get(self, request, *args, **kwargs):
        data = FilmCreateModel.objects.all()
        return render(request, 'filmview.html', {'data': data})

class film_detail(View):
    def get(self, request, *args, **kwargs):
        id_data = kwargs.get('id')
        data = FilmCreateModel.objects.get(id = id_data)
        return render(request, 'filmdetailview.html', {'data': data})


class FilmUpdate(View):
    def get(self, request, *args, **kwargs):
        id_data = kwargs.get('id')
        data = FilmCreateModel.objects.get(id = id_data)

        data_dict = {
            'films_name' : data.films_name,
            'release_date': data.release_date,
            'director': data.director
        }
        form_instance=FilmForm(initial=data_dict)
        return render(request, 'filmupdate.html', {'form':form_instance})
    def post(self, request, *args, **kwargs):
        form_instance=FilmForm(request.POST)

        if form_instance.is_valid():
            data=form_instance.cleaned_data
            id_data = kwargs.get('id')
            FilmCreateModel.objects.filter(id = id_data).update(**data)
            return redirect('/film_view/')


