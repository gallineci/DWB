from django.views.generic import ListView
from .models import Anuncio

class ListarAnuncios(ListView):
    model = Anuncio
    template_name = 'anuncio/listar.html'
    context_object_name = 'anuncios'
