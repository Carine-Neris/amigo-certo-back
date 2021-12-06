from django.urls import include, path
from rest_framework import routers
from .views import UsuariosViewSet, ListaUsuarios, AcompanhanteViewSet


router = routers.DefaultRouter()
router.register('cadastrar_usuario', UsuariosViewSet)
router.register('cadastrar_acompanhante', AcompanhanteViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('cadastrar_usuario/', ListaUsuarios.as_view())
]