from django.db import models

# Create your models here.
class Client(models.Model):
    idClient = models.IntegerField(blank=True)
    name = models.TextField(blank=True, null=True)
    prenom = models.TextField(blank=True, null=True)
    mail = models.TextField(blank=True, null=True)
    telephone = models.IntegerField(blank=True)
    facebook = models.TextField(blank=True, null=True)
    instagram = models.TextField(blank=True, null=True)