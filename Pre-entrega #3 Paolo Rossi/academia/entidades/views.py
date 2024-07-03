from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    return render(request,"entidades/index.html")

def comprar(request):
    contexto= {"comprar":Compras.objects.all()}
    return render(request,"entidades/comprar.html", contexto)

def projects(request):
    contexto= {"comprar":Visitantes.objects.all()}
    return render(request,"entidades/projects.html", contexto)

def producto(request):
    contexto= {"comprar":Productos.objects.all()}
    return render(request,"entidades/producto.html", contexto)

    #    contexto={"comprar": Comprar.objects.all()}