from django.shortcuts import render
from . import models
from . import serializers
from django.core.paginator import Paginator
from rest_framework import viewsets, generics
from rest_framework.response import Response



class UsersViewSet(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer

    
# class AcompanhanteViewSet(viewsets.ModelViewSet):
#     queryset = models.Acompanhante.objects.all()
#     serializer_class = serializers.AcompanhanteSerializer


class ListNecessidadesViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        queryset = models.Necessidades.objects.all()
        return queryset

    serializer_class = serializers.NecessidadesSerializer


# class ClienteViewSet(viewsets.ModelViewSet):
#     queryset = models.Cliente.objects.all()
#     serializer_class = serializers.ClienteSerializer
    
    
# class PerfilViewSet(viewsets.ModelViewSet):
#     queryset = models.Perfil.objects.all()
#     serializer_class = serializers.PerfilSerializer