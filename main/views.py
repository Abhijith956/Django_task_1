from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee
from .forms import EmployeeForm

# 🔹 Combined View
def employee_list(request):
    employees = Employee.objects.all()

    if request.method == 'POST':
        # handle Add Employee (modal)
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()

    return render(request, 'list.html', {'employees': employees, 'form': form})


# 🔹 Edit Employee (called by edit modal form)
def edit_employee(request, id):
    emp = get_object_or_404(Employee, id=id)
    if request.method == 'POST':
        emp.name = request.POST.get('name')
        emp.position = request.POST.get('position')
        emp.salary = request.POST.get('salary')
        if 'image' in request.FILES:  # only if user uploaded new image
            emp.image = request.FILES['image']

        emp.save()
        return redirect('employee_list')
