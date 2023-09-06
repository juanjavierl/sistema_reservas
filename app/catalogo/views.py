from django.shortcuts import render

# Create your views here.
def catalogo(request):
    user = "Javier"#declaracion de una variable
    return render(request,'catalogo.html',{'user':user})