from django.urls import include, path
from rest_framework import routers
from .views import  UsersViewSet, NecessidadesViewSet 


router = routers.DefaultRouter()
router.register('cadastrar-usuario', UsersViewSet)
router.register('cadastrar-necessidade', NecessidadesViewSet, base_name='necessidade')


urlpatterns = [
    path('', include(router.urls)),
    #path('cadastro-necessidade', NecessidadesView.as_view(), name='necessidades'),
]
