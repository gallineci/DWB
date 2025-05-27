from django.urls import path
from .views import ListarAnuncios, CriarAnuncio

urlpatterns = [
    path('', ListarAnuncios.as_view(), name='listar-anuncios'),
    path('novo/', CriarAnuncio.as_view(), name='cadastrar=-anuncio'),
]
