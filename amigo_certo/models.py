from django.db import models
from django.contrib.auth.models import User
from datetime import date


class Endereco(models.Model):
    rua = models.CharField(max_length=200)
    cidade = models.CharField(max_length=200)
    estado = models.CharField(max_length=200)
    cep = models.CharField(max_length=200)
    pais = models.CharField(max_length=200)
    
    def __str__(self):
        return self.cidade
