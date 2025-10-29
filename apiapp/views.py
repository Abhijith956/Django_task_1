from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from main.models import Employee
from .serializers import EmployeeSerializer
from django.shortcuts import get_object_or_404
from rest_framework.parsers import MultiPartParser, FormParser

# ✅ GET all employees or POST new one
class EmployeeListCreateAPIView(APIView):
    parser_classes = [MultiPartParser, FormParser] 
    def get(self, request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ✅ GET single employee, PUT (update), DELETE
class EmployeeDetailAPIView(APIView):
    def get(self, request, pk):
        emp = get_object_or_404(Employee, pk=pk)
        serializer = EmployeeSerializer(emp)
        return Response(serializer.data)

    def put(self, request, pk):
        emp = get_object_or_404(Employee, pk=pk)
        serializer = EmployeeSerializer(emp, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        emp = get_object_or_404(Employee, pk=pk)
        emp.delete()
        return Response({"message": "Employee deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
