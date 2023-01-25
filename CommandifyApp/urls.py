from django.urls import path, include

from .views import *


urlpatterns = [
    path('',home, name="home"),
    path('productsList',productsList,name="productsList"),
    path('clientsList',clientsList,name="clientsList"),
    path('commandsList',commandsList,name="commandsList"),

]
