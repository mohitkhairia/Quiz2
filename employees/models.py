from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)
    location = models.CharField(max_length=100)
    budget = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return self.name

class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name  = models.CharField(max_length=50)
    email      = models.EmailField(unique=True)
    date_joined= models.DateField()
    department = models.ForeignKey(Department, on_delete=models.PROTECT, related_name='employees')
    is_active  = models.BooleanField(default=True)
    salary     = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Attendance(models.Model):
    employee   = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='attendances')
    date       = models.DateField()
    status     = models.CharField(max_length=10, choices=[('Present','Present'),('Absent','Absent')])
    hours_worked = models.DecimalField(max_digits=4, decimal_places=2)

class Performance(models.Model):
    employee      = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='performances')
    review_period = models.CharField(max_length=20)  # e.g. "Q1 2025"
    score         = models.IntegerField()
    remarks       = models.TextField()