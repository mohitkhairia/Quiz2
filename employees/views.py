from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Department, Employee
from .serializers import DepartmentSerializer, EmployeeSerializer
from django.db.models import Avg
from django.urls import path

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.select_related('department').prefetch_related('attendances','performances')
    serializer_class = EmployeeSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['department__name', 'is_active']
    search_fields = ['first_name','last_name','email']
    ordering_fields = ['date_joined','salary']

    @action(detail=False, url_path='avg-salary-by-dept')
    def avg_salary_by_dept(self, request):
        data = Department.objects.annotate(avg_salary=Avg('employees__salary')).values('name','avg_salary')
        return Response(data)
    
def dashboard(request):
    return render(request, 'dashboard.html')

# add to urls.py:
path('dashboard/', dashboard),