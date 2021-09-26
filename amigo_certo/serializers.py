from rest_framework import serializers
from . import models
from django.contrib.auth.models import User



class EnderecoSerializer(serializers.ModelSerializer):
    rua = serializers.CharField(max_length=100)
    cidade =serializers.CharField(max_length=140)
    estado = serializers.CharField(max_length=140)
    cep = serializers.CharField(max_length=140)
    pais = serializers.CharField(max_length=140)

    class Meta:
        model = models.Endereco
        fields = ['id', 'rua', 'cidade', 'estado', 'cep', 'pais']