"""
URL configuration for FundTracker project.

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
from expense.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('expense/add', ExpenseCreateView.as_view(), name="expenseadd"),
    path('expense/all', ExpenseListView.as_view(), name="expenselist"),
    path('expense/<int:pk>/', ExpenseDetailView.as_view(), name="expensedetail"),
    path('expense/<int:pk>/delete', ExpenseRemoveView.as_view(), name="expenseremove"),
    path('expense/<int:pk>/update', ExpenseUpdateView.as_view(), name="expenseupdate"),
    path('expense/summary', ExpenceSummaryView.as_view(), name="expensesummary")
]
