from django.urls import path
from . import views

urlpatterns = [
    path('main/', views.employee_list, name='employee_list'),
    path('edit/<int:id>/', views.edit_employee, name='edit_employee'),

]