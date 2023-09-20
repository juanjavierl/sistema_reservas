
from . import views
from django.urls import path


urlpatterns = [
    path('', views.catalogo, name='catalogo'),
    path('produt/',views.productos,name='productos'),
    path('producto/<int:id_producto>',views.detalleProducto,name='productoDetalle'),
] 