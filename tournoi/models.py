from django.db import models

class Equipe(models.Model):
    nom = models.CharField(max_length=120, unique=True)
    promo = models.CharField(max_length=120)

    def __str__(self):
        return self.nom


class Match(models.Model):
    equipe_domicile = models.ForeignKey(
        Equipe, 
        on_delete=models.CASCADE, 
        related_name='matchs_domicile'
    )
    equipe_visiteuse = models.ForeignKey(
        Equipe, 
        on_delete=models.CASCADE, 
        related_name='matchs_visiteur'
    )
    date = models.DateField(max_length=50)
    
    status = models.CharField(max_length=20, default="EN_ATTENTE")
    
    score_domicile = models.IntegerField(null=True, blank=True)
    score_visiteuse = models.IntegerField(null=True, blank=True)

    @property
    def score(self):
        if self.score_domicile is None or self.score_visiteuse is None:
            return None
        return f"{self.score_domicile}-{self.score_visiteuse}"

    def __str__(self):

        if self.status == "EN_ATTENTE" or self.score is None:
            return f"{self.equipe_domicile} - {self.equipe_visiteuse} : à jouer"
        
        return f"{self.equipe_domicile} : {self.score}"
