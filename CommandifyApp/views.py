from django.contrib.sites import requests
from django.shortcuts import render
import json

<<<<<<< HEAD
=======
#Paths
productFile_Path = "products.json"
clientFile_Path = "clients.json"
commandFile_Path = "commands.json"



>>>>>>> ac80349eec2749ce92fd9726ea05b5d784ff53a5
# Create your views here.
def home(request):
    return render(request, 'home.html')


def productsList(request):
    data = requests.get('http://localhost:5000/api/product_list').json()
    return render(request, 'productsList.html', data)

def clientsList(request):
    data = requests.get('http://localhost:5000/api/client_list').json()
    return render(request, 'clientsList.html',data)


def commandsList(request):
    data = requests.get('http://localhost:5000/api/order_list').json()
    return render(request, 'commandsList.html',data)

