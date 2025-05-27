from django.db import models

class Anuncio(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='anuncios/', blank=True, null=True)

    def __str__(self):
        return self.titulo
