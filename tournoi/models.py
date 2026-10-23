from django.db import models

class Equipe(models.Model):

    nom = models.CharField(max_length=120,unique=True)
    promo = models.CharField(max_length=120)

    def __str__(self):
        return f"{self.nom} ({self.promo})"
