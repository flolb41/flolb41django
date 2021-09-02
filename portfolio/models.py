from django.db import models


class Portfolio(models.Model):
    nom = models.CharField(max_length=200)
    image = models.ImageField(upload_to='static/portfolio/images/')
    description = models.TextField(blank=True)
    lien = models.URLField(max_length=200)

    def __str__(self):
        return self.nom
