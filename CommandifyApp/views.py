from django.shortcuts import render
import json

#Paths
productFile_Path = "products.json"
clientFile_Path = "clients.json"
commandFile_Path = "commands.json"



# Create your views here.
def home(request):
    return render(request, 'home.html')


def productsList(request):
    return render(request, 'productsList.html')

def clientsList(request):
    with open(clientFile_Path, 'r') as file:
        data = json.load(file)
    data = {"clients":data.get("clients", [])}
    return render(request, 'clientsList.html',data)


def commandsList(request):
    with open(commandFile_Path, 'r') as file:
        data = json.load(file)
    data = {"commands":data.get("clients", [])}
    return render(request, 'commandsList.html',data)


def clientDetails(request):
    return render(request, 'clientDetails.html')
