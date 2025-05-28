from django.db import models
from veiculo.models import Veiculo
from django.contrib.auth.models import User

class Anuncio(models.Model):
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE, related_name='anuncios')
    anunciante = models.ForeignKey(User, on_delete=models.CASCADE, related_name='anuncios')
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.titulo} - R$ {self.preco:.2f}'