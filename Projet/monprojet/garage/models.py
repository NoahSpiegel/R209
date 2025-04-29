from django.db import models

# Create your models here.
class Voiture(models.Model):
    marque = models.CharField(max_length=100)
    modele = models.CharField(max_length=100)
    annee = models.CharField(max_length=20)
    couleur = models.CharField(max_length=30)
    immatriculation = models.CharField(max_length=30)

    def __str__(self):
        chaine = f"{self.marque} {self.modele} de l'année {self.annee} de couleur {self.couleur} immatriculée {self.immatriculation}"
        return chaine