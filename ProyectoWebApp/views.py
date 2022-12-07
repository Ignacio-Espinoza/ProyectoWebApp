from django.shortcuts import render, HttpResponse
from tienda.models import Producto

# Create your views here.

def home(request):
    return render(request,'ProyectoWebApp/home.html')

def tienda(request):
    productos=Producto.objects.all()
    return render(request,'ProyectoWebApp/tienda.html',{"tienda":productos})

def contacto(request):
    return render(request,'ProyectoWebApp/contacto.html')