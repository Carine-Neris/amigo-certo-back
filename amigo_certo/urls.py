from django.urls import include, path
from rest_framework import routers
from .views import  UsersViewSet, NecessidadesViewSet 
from rest_framework.authtoken.views import obtain_auth_token


router = routers.DefaultRouter()
router.register('cadastrar-usuario', UsersViewSet)
router.register('cadastrar-necessidade', NecessidadesViewSet, base_name='necessidade')


urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
