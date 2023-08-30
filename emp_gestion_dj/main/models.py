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

#creer en oracle sous forme de table: main_tribe
class Tribe(models.Model):
    id_trb = models.CharField(primary_key=True, max_length=10)
    intitule_trb = models.CharField(max_length=200)
    resp_trb = models.CharField(max_length=200)

    def __str__(self):
        return self.intitulé_trb
