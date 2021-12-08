from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from . import models
from . import serializers



class UsersViewSet(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer


class NecessidadesViewSet(viewsets.ModelViewSet):
    
    def get_queryset(self):
        queryset = models.Necessidades.objects.all()
        return queryset

    serializer_class = serializers.NecessidadesSerializer
    permission_classes = [IsAuthenticated]


