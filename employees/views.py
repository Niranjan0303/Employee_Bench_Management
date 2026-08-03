from django.shortcuts import render, redirect, get_object_or_404
import pandas as pd
from .models import Employee
from .forms import EmployeeForm
 
 
# Dashboard
def dashboard(request):
 
    employees = Employee.objects.all()
 
    total_employees = employees.count()
 
    total_customers = employees.values(
        "customer_name"
    ).distinct().count()
 
    profiles_shared = employees.exclude(
        customer_name=""
    ).count()
 
    rejected = employees.filter(
        profile_status__iexact="Rejected"
    ).count()
 
    context = {
        "total_employees": total_employees,
        "total_customers": total_customers,
        "profiles_shared": profiles_shared,
        "rejected": rejected,
        "employees": employees.order_by("-id")[:5],
    }
 
    return render(
        request,
        "dashboard.html",
        context,
    )
 
 
# Employee List
def employee_list(request):
    employees = Employee.objects.all().order_by("employee_id")
 
    context = {
        "employees": employees
    }
 
    return render(request, "employees/employee_list.html", context)
 
 
# Add Employee
def add_employee(request):
 
    if request.method == "POST":
 
        form = EmployeeForm(request.POST)
 
        if form.is_valid():
            form.save()
            return redirect("employee_list")
 
    else:
 
        form = EmployeeForm()
 
    context = {
        "form": form
    }
 
    return render(request, "employees/add_employee.html", context)
 
 
# Edit Employee
def edit_employee(request, id):
 
    employee = get_object_or_404(Employee, id=id)
 
    if request.method == "POST":
 
        form = EmployeeForm(request.POST, instance=employee)
 
        if form.is_valid():
            form.save()
            return redirect("employee_list")
 
    else:
 
        form = EmployeeForm(instance=employee)
 
    context = {
        "form": form
    }
 
    return render(request, "employees/edit_employee.html", context)
 
 
# Delete Employee
def delete_employee(request, id):
 
    employee = get_object_or_404(Employee, id=id)
 
    if request.method == "POST":
        employee.delete()
        return redirect("employee_list")
 
    context = {
        "employee": employee
    }
 
    return render(request, "employees/delete_employee.html", context)

def upload_excel(request):
 
    if request.method == "POST":
 
        excel_file = request.FILES["excel_file"]
 
        df = pd.read_excel(excel_file)
 
        for _, row in df.iterrows():
 
            Employee.objects.create(
 
                employee_id=row["employee_id"],
                employee_name=row["employee_name"],
                employee_email=row["employee_email"],
                total_experience=row["total_experience"],
                primary_skill=row["primary_skill"],
                secondary_skill=row["secondary_skill"],
                cm_name=row["cm_name"],
                profile_status=row["profile_status"],
                customer_name=row["customer_name"],
                date_shared=row["date_shared"],
                project_owner=row["project_owner"],
 
            )
 
        return redirect("employee_list")
 
    return render(request, "upload_excel.html")