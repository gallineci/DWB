from django.urls import path
from veiculo.views import *

urlpatterns = [
    path ('',ListarVeiculos.as_view(), name = 'listar-veiculos'),
    path ('novo/', CriarVeiculos.as_view(), name='criar-veiculos'),
    path ('fotos/<str:arquivo>/', FotoVeiculo.as_view(), name='foto-veiculo'),
    path ('<int:pk>/', EditarVeiculo.as_view(), name='editar-veiculo'),
    path ('deletar/<int:pk>/', DeletarVeiculo.as_view(), name='deletar-veiculo'),
]