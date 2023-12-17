from django.urls import path
from galeria.views import index, cadastro, empresa, login, contato, orcamento_sucesso, area_cliente, planos, login_servidor, area_servidor, equipamento
from . import views 
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('cadastro/', cadastro, name='cadastro'),
    path('empresa/', empresa, name='empresa'),
    path('login/', login, name='login'),
    path('contato/', contato, name='contato'),
    path('planos/',planos, name = 'planos'),
    path('login_servidor/', login_servidor, name = 'login_servidor'),
    path('area_cliente/', area_cliente, name = 'area_cliente'),
    path('area_servidor/', area_servidor, name = 'area_servidor'),
    path('equipamento/', equipamento, name='equipamento'),
    path('index/', views.index, name='index'),
    path('enviar_orcamento/', views.enviar_orcamento, name='enviar_orcamento'),
    path('orcamento_sucesso/', views.orcamento_sucesso, name='orcamento_sucesso'),
    path('cadastrar/', views.cadastrar_usuario, name = 'cadastrar_usuario'),
    path('instalacao/', views.instalacao, name = 'instalacao'),
    path('login/', views.login, name='login'),
    path('area_cliente/', views.area_cliente, name='area_cliente'),
    path('area_servidor/', views.area_servidor, name = 'area_servidor' ),
    path('comentar/', views.comentar, name = 'comentar'),
    path('login/', views.login, name='login'),
]
