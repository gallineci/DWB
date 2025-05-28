from django.views.generic import ListView
from .models import Anuncio
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import FormularioAnuncio
from django.views import View
from django.views.generic.edit import UpdateView, DeleteView

class ListarAnuncios(ListView):
    model = Anuncio
    template_name = 'anuncio/listar.html'
    context_object_name = 'anuncios'

class CriarAnuncio(CreateView):
    model = Anuncio
    form_class = FormularioAnuncio
    template_name = 'anuncio/novo.html'
    success_url = reverse_lazy('listar-anuncios')

    def form_valid(self, form):
        form.instance.anunciante = self.request.user
        return super().form_valid(form)
    

class EditarAnuncio(UpdateView):
    model = Anuncio
    form_class = FormularioAnuncio
    template_name = 'anuncio/editar.html'
    success_url = reverse_lazy('listar-anuncios')

class DeletarAnuncio(DeleteView):
    model = Anuncio
    template_name = 'anuncio/deletar.html'
    success_url = reverse_lazy('listar-anuncios')