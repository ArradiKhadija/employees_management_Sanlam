from rest_framework import serializers
from .models import *
from django.contrib.auth.models import *

import cx_Oracle
##auth

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id', 'nomComplet', 'email', 'contact', 'adresse','poste','salaire')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')  # Utiliser les champs appropriés de User

class TribeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tribe
        fields = ('id_trb', 'intitule_trb', 'resp_trb')


class VacationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacation
        fields = ('id_vac', 'id_emp_vac','type_vac','start_vac','end_vac','duration_vac','reason_vac','approbateur_vac')


