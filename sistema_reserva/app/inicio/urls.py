
from . import views
from django.urls import include, path

urlpatterns = [
    path('', views.inicio, name='inicio')
]  