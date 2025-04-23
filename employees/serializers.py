from rest_framework import serializers
from .models import Department, Employee, Attendance, Performance

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department; fields = '__all__'

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance; fields = '__all__'

class PerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Performance; fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer(read_only=True)
    attendances = AttendanceSerializer(many=True, read_only=True)
    performances = PerformanceSerializer(many=True, read_only=True)
    class Meta:
        model = Employee
        fields = '__all__'