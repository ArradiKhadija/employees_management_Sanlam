from django.shortcuts import render
from rest_framework import viewsets
from .serializers import EmployeeSerializer
from .models import Employee


# Create your views here.

class EmployeeViewSet(viewsets.ModelViewSet):
    serializer_class    =EmployeeSerializer
    queryset = Employee.objects.all().order_by('-id')
