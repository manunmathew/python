from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from .models import *
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
