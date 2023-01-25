from django.urls import path, include

from .views import *


urlpatterns = [
    path('',home, name="home"),
    path('clientsList',clientsList,name="clientsList"),
    path('commandsList',commandsList,name="commandsList"),
    path('client/<int:n_client>/',clientDetails,name="clientDetails"),

]
