# apiapp/urls.py
from django.urls import path
from .views import EmployeeListCreateAPIView, EmployeeDetailAPIView
urlpatterns = [
    path('employees/', EmployeeListCreateAPIView.as_view(), name='employee_list_api'),
    path('employees/<int:pk>/', EmployeeDetailAPIView.as_view(), name='employee_detail_api'),
]