from django.shortcuts import render
import datetime
# Create your views here.
def inicio(request):
    fecha_hora = datetime.datetime.now()
    nombre = "User"
    nombres = ['jhon', 'ana','pepe']
    #print(nombres)
    datos = {
        'fecha_hora':fecha_hora,
        'nombre':nombre,
        'nombres':nombres
        }
    return render(request, 'base.html',datos)