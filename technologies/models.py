from django.db import models

# Create your models here.


class Technologies(models.Model):
    nom = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='static/technologies/images/')
    description = models.TextField(blank=True)
    frontend = models.BooleanField(default=False)
    backend = models.BooleanField(default=False)

    def __str__(self):
        return self.nom
