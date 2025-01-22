"""
URL configuration for ExpenseTracker project.

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
from expense_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',views.SignUpView.as_view(),name="register"),
    path('signin/',views.SignInView.as_view(),name="signin"),
    path('index/',views.IndexView.as_view(),name="index"),
    path('signout/',views.SignOutView.as_view(),name="signout"),
    path('expense/add/',views.ExpenseCreateView.as_view(),name="expenseadd"),
    path('expense/<int:pk>/remove',views.ExpenseDeleteView.as_view(),name="expenseremove"),
    path('expense/<int:pk>/edit', views.ExpenseUpdateView.as_view(), name="expenseedit")
]
