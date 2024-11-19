from django.shortcuts import render, redirect
from .models import Cliente

# Create your views here.

def inicio_vista(request):
    losClientes=Cliente.objects.all()
    return render(request,'gestionarCliente.html',{'misClientes':losClientes})

def registrarCliente(request):
    id_cliente=request.POST["numidcliente"]
    nombre=request.POST["txtnombre"]
    apellido=request.POST["txtapellido"]
    fecha_nac=request.POST["txtfechanac"]
    correo_elec=request.POST["txtcorreoelec"]
    telefono=request.POST["numtelefono"]
    direccion=request.POST["txtdireccion"]

    guardarCliente=Cliente.objects.create(id_cliente=id_cliente,nombre=nombre,apellido=apellido,fecha_nac=fecha_nac,correo_elec=correo_elec,telefono=telefono,direccion=direccion)

    return redirect('/')

def seleccionarCliente(request,id_cliente):
    Cliente_=Cliente.objects.get(id_cliente=id_cliente)
    return render(request,"editarCliente.html",{"misClientes":Cliente_})

def editarCliente(request):
    id_cliente=request.POST["numidcliente"]
    nombre=request.POST["txtnombre"]
    apellido=request.POST["txtapellido"]
    fecha_nac=request.POST["txtfechanac"]
    correo_elec=request.POST["txtcorreoelec"]
    telefono=request.POST["numtelefono"]
    direccion=request.POST["txtdireccion"]

    Cliente_=Cliente.objects.get(id_cliente=id_cliente)

    Cliente_.nombre=nombre
    Cliente_.apellido=apellido
    Cliente_.fecha_nac=fecha_nac
    Cliente_.correo_elec=correo_elec
    Cliente_.telefono=telefono
    Cliente_.direccion=direccion
    Cliente_.save()

    return redirect('/')

def borrarCliente(request,id_cliente):
    Cliente_=Cliente.objects.get(id_cliente=id_cliente)
    Cliente_.delete()

    return redirect('/')
