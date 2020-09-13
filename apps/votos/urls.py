from django.urls import path
from .views import mostrarVotos, votar

urlpatterns = [
    path('mostrar-votos', mostrarVotos, name='mostrarVotos'),
    path('votar/', votar, name='votar'),
]