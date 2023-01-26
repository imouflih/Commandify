from django.urls import path, include

from .views import *


urlpatterns = [
    path('',home, name="home"),
    path('productsList',productsList,name="productsList"),
    path('clientsList',clientsList,name="clientsList"),
    path('commandsList',commandsList,name="commandsList"),
    path('productsList',ajoutProduit,name="ajoutProduit"),
    path('clientsList',ajoutClient,name="ajoutClient"),
    path('commandsList',ajoutCommande,name="ajoutCommande"),
    path('productsList',modifProduit,name="modifProduit"),
    path('clientsList',modifClient,name="modifClient"),
    path('commandsList',modifCommande,name="modifCommande"),
    path('productsList',deleteProduit,name="deleteProduit"),
    path('clientsList',deleteClient,name="deleteClient"),


]
