
from . import views
from django.urls import include, path

urlpatterns = [
    path('', views.clientes, name='clientes')
]  