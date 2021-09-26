from django.shortcuts import render
from . import models
from . import serializers
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from rest_framework import viewsets
from rest_framework.response import Response


class EnderecoViewSet(viewsets.ModelViewSet):
    queryset = models.Endereco.objects.all()
    serializer_class = serializers.EnderecoSerializer


