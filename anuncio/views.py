from django.views.generic import ListView
from .models import Anuncio
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import FormularioAnuncio

class ListarAnuncios(ListView):
    model = Anuncio
    template_name = 'anuncio/listar.html'
    context_object_name = 'anuncios'

class CriarAnuncio(CreateView):
    model = Anuncio
    form_class = FormularioAnuncio
    template_name = 'anuncio/novo.html'
    success_url = reverse_lazy('listar-anuncios')
