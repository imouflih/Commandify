from django.shortcuts import render
from .models import Client
import json

# Create your views here.
def home(request):
    return render(request, 'home.html')


def clientsList(request):
    with open("C:/Users/ilias/Desktop/Commandify/clients.json", 'r') as file:
        data = json.load(file)
    data = {"clients":data.get("clients", [])}
    return render(request, 'clientsList.html',data)


def commandsList(request):
    with open("C:/Users/ilias/Desktop/Commandify/commands.json", 'r') as file:
        data = json.load(file)
    data = {"commands":data.get("clients", [])}
    return render(request, 'commandsList.html',data)


def clientDetails(request, n_client):
    client = Client.objects.get(n_client=n_client)
    context = {
        "object": client
    }
    return render(request, 'clientDetails.html', context)
