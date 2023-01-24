from django.shortcuts import render
from .models import Client

# Create your views here.
def home(request):
    var = {"clients":[{"idClient" : 1,
                        "nom":"Durem",
                        "prenom":"Alexandre",
                        "mail":"Alexandre@example.com",
                        "telephone":985050505,
                        "facebook":"@Alexandre",
                        "instagram":"@Alexandre"},
                        {"idClient": 2,
                        "nom": "Hamid",
                        "prenom": "SimoVI",
                        "mail": "SimoVI@example.com",
                        "telephone": 985050505,
                        "facebook": "@SimoVI",
                        "instagram": "@SimoVI"}
              ]}
    return render(request,'home.html',var)

def login(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')

def clientDetails(request, idClient):
    client = Client.objects.get(idClient=idClient)
    context = {
        "object" : client
    }
    return render(request, 'clientDetails.html',context)

