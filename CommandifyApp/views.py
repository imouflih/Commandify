from django.contrib.sites import requests
from django.shortcuts import render
import json

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

