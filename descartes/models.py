from django.db import models

from ecopontos.models import Ecopontos
from descartadores.models import Descartadores


class Descartes(models.Model):
    nome = models.CharField(default='-', max_length=30)
    tipo = models.CharField(default='-', max_length=15)
    quantidade = models.CharField(default=0, max_length=20)
    descartador = models.ForeignKey(Descartadores, on_delete=models.CASCADE)
    ecoponto = models.ForeignKey(Ecopontos, on_delete=models.CASCADE)
