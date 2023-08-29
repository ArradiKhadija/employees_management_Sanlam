from rest_framework import serializers
from .models import Employee
from django.contrib.auth.models import User

import cx_Oracle
##auth

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id', 'nomComplet', 'email', 'contact', 'adresse')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')  # Utiliser les champs appropriés de User
