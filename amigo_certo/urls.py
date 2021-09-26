from django.urls import include, path
from rest_framework import routers
from .views import EnderecoViewSet

api_routers = routers.SimpleRouter()

api_routers.register('endereco', EnderecoViewSet)

urlpatterns = api_routers.urls