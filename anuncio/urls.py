from django.urls import path
from .views import ListarAnuncios

urlpatterns = [
    path('', ListarAnuncios.as_view(), name='listar-anuncios'),
]
