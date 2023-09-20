from django.shortcuts import render

# Create your views here.
def catalogo(request):
    user = "Javier"#declaracion de una variable
    return render(request,'catalogo.html',{'user':user})



def productos(request):
    context = {}
    return render(request, "productos.html",context)

def detalleProducto(request, id_producto):
    context = {
        'id_producto':id_producto
    }
    return render(request, "productoDetalle.html",context)