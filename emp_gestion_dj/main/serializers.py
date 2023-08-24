from rest_framework import serializers
from .models import Employee
import cx_Oracle
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model   =Employee
        fields  = ('id','nomComplet','email','contact','adresse')

