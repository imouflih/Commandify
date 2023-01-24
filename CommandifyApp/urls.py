from django.urls import path, include

from .views import *


urlpatterns = [
    path('',home, name="home"),
    path('login',login,name="login"),
    path('register',register,name="register"),
    path('client/<int:idClient>/',clientDetails,name="clientDetails"),

]
