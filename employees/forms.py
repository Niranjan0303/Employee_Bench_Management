from django import forms
from .models import Employee
 
 
class EmployeeForm(forms.ModelForm):
 
    class Meta:
        model = Employee
        fields = "__all__"
 
        widgets = {
            "employee_id": forms.TextInput(attrs={"class": "form-control"}),
            "employee_name": forms.TextInput(attrs={"class": "form-control"}),
            "employee_email": forms.EmailInput(attrs={"class": "form-control"}),
            "total_experience": forms.NumberInput(attrs={"class": "form-control"}),
            "primary_skill": forms.TextInput(attrs={"class": "form-control"}),
            "secondary_skill": forms.TextInput(attrs={"class": "form-control"}),
            "cm_name": forms.TextInput(attrs={"class": "form-control"}),
            "profile_status": forms.TextInput(attrs={"class": "form-control"}),
            "customer_name": forms.TextInput(attrs={"class": "form-control"}),
            "date_shared": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date"
                }
            ),
            "project_owner": forms.TextInput(attrs={"class": "form-control"}),
        }