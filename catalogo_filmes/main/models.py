from django.db import models
from datetime import datetime as dt
# Create your models here.

class ProjetoDjango(models.Model):
    # Aqui definimos as colunas que teremos em nosso banco de dados
    titulo_filme = models.CharField("Título do Filme",max_length=50)
    genero = models.CharField("Gênero", max_length=50)
    avaliacao_IMDb = models.DecimalField("Avaliação IMDb", decimal_places=2, max_digits=100)
    data = models.DateTimeField("Data Lançamento", default=dt.now())

    def __str__(self):
        return self.titulo_filme
