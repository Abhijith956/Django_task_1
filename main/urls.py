from django.urls import path
from . import views

urlpatterns = [
    path('', views.employee_list, name='employee_list'),
    path('add/', views.employee_list, name='add_employeee'),
    path('edit/<int:id>/', views.edit_employee, name='edit_employee'),

]