from django.db import models
from django.contrib.auth.models import User


class Evento(models.Model):
    nome = models.CharField(max_length=155)
    data = models.CharField(max_length=10)
    inicio = models.CharField(max_length=5)
    final = models.CharField(max_length=5)
    endereco = models.CharField(max_length=155)
    endereco2 = models.CharField(max_length=155, blank=True, null=True)
    cep = models.CharField(max_length=50)
    gestor = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.nome}'


class Artista(models.Model):
    nome = models.CharField(max_length=155)
    inicio = models.CharField(max_length=5)
    final = models.CharField(max_length=5)
    foto = models.ImageField(upload_to='artistas/img/',)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    evento = models.ForeignKey(Evento, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.nome}'