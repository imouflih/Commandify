import requests
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
    response = requests.get('http://localhost:5000/api/product_list')
    data = json.loads(response.text)
    return render(request, 'productsList.html', data)

def clientsList(request):
    response = requests.get('http://localhost:5000/api/client_list')
    data = json.loads(response.text)
    return render(request, 'clientsList.html',data)


def commandsList(request):
    response = requests.get('http://localhost:5000/api/order_list')
    data = json.loads(response.text)
    return render(request, 'commandsList.html',data)

def ajoutClient(request):
    if request.method == 'POST':
        data = request.POST
        requests.put('http://localhost:5000/api/create_client', json=data)
    return render(request, 'clientsList.html')

def ajoutProduit(request):
    if request.method == 'POST':
        data = request.POST
        requests.post('http://localhost:5000/api/create_product', json=data)
    return render(request, 'productsList.html', {"data":data})

def ajoutCommande(request):
    if request.method == 'POST':
        data = request.POST
        requests.post('http://localhost:5000/api/create_order', json=data)
    return render(request, 'commandsList.html')

def modifClient(request):
    if request.method == 'POST':
        data = request.POST
        requests.put('http://localhost:5000/api/modify_client/'+data["n_client"], json=data)
    return render(request, 'clientsList.html')

def modifProduit(request):
    if request.method == 'POST':
        data = request.POST
        requests.put('http://localhost:5000/api/modify_product/'+data["n_produit"], json=data)
    return render(request, 'productsList.html', {"data":data})

def modifCommande(request):
    if request.method == 'POST':
        data = request.POST
        requests.post('http://localhost:5000/api/modify_order/'+data["n_commande"], json=data)
    return render(request, 'commandsList.html')

def deleteClient(request,n_commande):
    requests.delete('http://localhost:5000/api/delete_client/'+n_commande)
    return render(request, 'commandsList.html')

def deleteProduit(request,n_commande):
    requests.delete('http://localhost:5000/api/delete_product/'+n_commande)
    return render(request, 'commandsList.html')
