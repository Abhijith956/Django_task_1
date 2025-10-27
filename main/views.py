from django.shortcuts import render, get_object_or_404, redirect
from .models import Employee
from .forms import EmployeeForm

# ---------------- List View ----------------
def employee_list(request):
    employees = Employee.objects.all()  # fetch all employees
    return render(request, 'list.html', {'employees': employees})

# ---------------- Add View ----------------
def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')  # reload table after adding
    else:
        form = EmployeeForm()
    return render(request, 'add.html', {'form': form})

# ---------------- Edit View ----------------
def edit_employee(request, id):
    employee = get_object_or_404(Employee, id=id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')  # reload table after editing
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'edit.html', {'form': form})
