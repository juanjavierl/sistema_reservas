from django.shortcuts import render
import datetime
# Create your views here.
def inicio(request):
    fecha_hora = datetime.datetime.now()
    nombre = "Administrador"
    datos = {
        'fecha_hora':fecha_hora,
        'nombre':nombre
        }
    return render(request, 'base.html',datos)