from django.shortcuts import render
from . import models
from . import serializers
from django.core.paginator import Paginator
from rest_framework import viewsets, generics
from rest_framework.response import Response



class UsuariosViewSet(viewsets.ModelViewSet):
    queryset = models.Usuario.objects.all()
    serializer_class = serializers.UsuarioSerializer

class ListaUsuarios(generics.ListAPIView):
    
    def get_queryset(self):
        queryset = models.Usuario.objects.all()
        return queryset
    serializer_class = serializers.UsuarioSerializer
    
    
class AcompanhanteViewSet(viewsets.ModelViewSet):
    queryset = models.Acompanhante.objects.all()
    serializer_class = serializers.AcompanhanteSerializer
