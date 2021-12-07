from django.urls import include, path
from rest_framework import routers
from .views import  UsersViewSet 


router = routers.DefaultRouter()
router.register('cadastrar_usuario', UsersViewSet)
# router.register('cadastrar_acompanhante', AcompanhanteViewSet, base_name="cadastro-acompanhante")
# router.register('cadastrar_cliente', ClienteViewSet, base_name="cadastro-cliente")
# router.register('lista_necessidades', ListNecessidadesViewSet, base_name="necessidades")
# router.register('cadastrar_perfil', PerfilViewSet, base_name="cadastro-perfil")

urlpatterns = [
    path('', include(router.urls)),
]