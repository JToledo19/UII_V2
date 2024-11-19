from django.shortcuts import render
from .models import
def inicio_vista(request):
    Lista=Productos.objects.all()
    return request (request,"index.html",{{listaP}})

# Create your views here.
