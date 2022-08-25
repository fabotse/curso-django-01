from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('colaborador/<str:pk>', views.colaborador, name='colaborador'),
    path('criar_chamado/<str:pk>', views.criarChamado, name='criarChamado'),
    path('update_chamado/<str:pk>', views.updateChamado, name='updateChamado'),
    path('deletar_chamado/<str:pk>', views.deletarChamado, name='deletarChamado')
    
]
