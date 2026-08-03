from django.db import models
 
class Employee(models.Model):
    employee_id = models.CharField(max_length=20, unique=True)
    employee_name = models.CharField(max_length=100)
    employee_email = models.EmailField()
    total_experience = models.DecimalField(max_digits=4, decimal_places=1)
    primary_skill = models.CharField(max_length=100)
    secondary_skill = models.CharField(max_length=100, blank=True)
    cm_name = models.CharField(max_length=100)
    profile_status = models.CharField(max_length=100)
    customer_name = models.CharField(max_length=100)
    date_shared = models.DateField()
    project_owner = models.CharField(max_length=100)
 
    def __str__(self):
        return f"{self.employee_id} - {self.employee_name}"
 