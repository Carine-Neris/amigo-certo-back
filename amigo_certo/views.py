from . import models
from . import serializers
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status



class UsersViewSet(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer


class NecessidadesViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        queryset = models.Necessidades.objects.all()
        return queryset

    serializer_class = serializers.NecessidadesSerializer


# class NecessidadesView(APIView):
    
#     def get(self, format=None):
        
#         necessidades = models.Necessidades.objects.all()
#         serializer = serializers.NecessidadesSerializer(necessidades, many=True)
#         return Response(serializer.data)

#     def post(self, request):
    
#         serializer = serializers.NecessidadesSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=ValueError):
#             serializer.create(validated_data=request.data)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.error_messages,
#                         status=status.HTTP_400_BAD_REQUEST)