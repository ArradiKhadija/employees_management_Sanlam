from django.db import models

# Create your models here.
class Employee(models.Model):
    id=models.AutoField(primary_key=True)
    nomComplet = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    contact = models.CharField(max_length=100)
    adresse = models.TextField()

    def __str__(self):
        return self.nomComplet

