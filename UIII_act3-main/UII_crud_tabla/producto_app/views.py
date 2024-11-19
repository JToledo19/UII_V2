from django.shortcuts import render, redirect
from .models import Producto

# Create your views here.

def inicio_vista(request):
    losproductos=Producto.objects.all()
    return render(request,'gestionarProducto.html',{'misproductos':losproductos})

def registrarProducto(request):
    id_producto=request.POST["numidproducto"]
    nombre=request.POST["txtnombre"]
    marca=request.POST["txtmarca"]
    tipo=request.POST["txttipo"]
    volumen=request.POST["numvolumen"]
    precio=request.POST["numprecio"]
    notas_olfativas=request.POST["txtnotas"]

    guardarproducto=Producto.objects.create(id_producto=id_producto,nombre=nombre,marca=marca,tipo=tipo,volumen=volumen,precio=precio,notas_olfativas=notas_olfativas)

    return redirect('/')

def seleccionarProducto(request,id_producto):
    producto=Producto.objects.get(id_producto=id_producto)
    return render(request,"editarProducto.html",{"misproductos":producto})

def editarProducto(request):
    id_producto=request.POST["numidproducto"]
    nombre=request.POST["txtnombre"]
    marca=request.POST["txtmarca"]
    tipo=request.POST["txttipo"]
    volumen=request.POST["numvolumen"]
    precio=request.POST["numprecio"]
    notas_olfativas=request.POST["txtnotas"]

    producto=Producto.objects.get(id_producto=id_producto)

    producto.nombre=nombre
    producto.marca=marca
    producto.tipo=tipo
    producto.volumen=volumen
    producto.precio=precio
    producto.notas_olfativas=notas_olfativas
    producto.save()

    return redirect('/')

def borrarProducto(request,id_producto):
    producto=Producto.objects.get(id_producto=id_producto)
    producto.delete()

    return redirect('/')