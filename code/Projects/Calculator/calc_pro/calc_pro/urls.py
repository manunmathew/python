"""
URL configuration for calc_pro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from calc_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('first/', First.as_view() ),
    path('pettu/', Second.as_view()),
    path('django/', Template1.as_view()),
    path('index/', Index.as_view()),
    path('add/', Addition.as_view()),
    path('sub/', Subtraction.as_view()),
    path('multiply/', Multiplication.as_view()),
    path('div/', Division.as_view()),
    path('area_circle/', AreaOfCircle.as_view()),
    path('area_triangle/', AreaOfTriangle.as_view()),
    path('addview/', Add_display_view.as_view()),
    path('subview/', Sub_display_view.as_view()),
]
