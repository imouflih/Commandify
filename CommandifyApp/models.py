from django.db import models

# Create your models here.
class Client(models.Model):
    n_client = models.IntegerField(blank=True)
    nom_client = models.TextField(blank=True, null=True)
    add_postale = models.TextField(blank=True, null=True)
    add_email = models.TextField(blank=True, null=True)
    tel = models.IntegerField(blank=True)
    facebook = models.TextField(blank=True, null=True)
    instagram = models.TextField(blank=True, null=True)
    fidelite = models.TextField(blank=True, null=True)

