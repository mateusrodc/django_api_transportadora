"""helloworld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from website.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', do_logout, name='logout'),
    path('index/', index, name='index'),
    path('autenticar/', do_login, name="autenticar"),
    
    path('funcionario/', listafuncionarios, name='home_funcionario'),
    path('funcionario/add', cadastrarfuncionarios, name='create_funcionario'),
    path('funcionario/salvar', salvarfuncionarios, name='salvar_funcionario'),
    path('funcionario/editar/<int:id>/',editarfuncionarios,name='editar_funcionario'),
    path('funcionario/remover/<int:id>/',removerfuncionarios,name='remover_funcionario'),

    path('veiculo/', lista_veiculos, name="lista_veiculos"),
    path('veiculo/add', criar_veiculo, name='criar_veiculo'),
    path('veiculo/salvar',salvar_veiculo,name='salvar_veiculo'),
    path('veiculo/editar/<int:id>/',editar_veiculos,name='editar_veiculo'),
    path('veiculo/remover/<int:id>/',remover_veiculos,name='remover_veiculo'),

    path('atendimento/', listaAtendimento, name="lista_atendimentos"),
    path('atendimento/add',cadastrarAtendimento,name="create_atendimentos"),
    path('atendimento/salvar',salvarAtendimento,name="salvar_atendimento"),
    path('atendimento/editar/<int:id>/',editarAtendimento,name="editar_atendimento"),
    path('atendimento/remover/<int:id>/',removerAtendimento,name="remover_atendimento"),

    path('estudante/',listaEstudante,name="lista_estudantes"),
    path('estudante/add',cadastrarEstudante,name="create_estudante"),
    path('estudante/salvar',salvarEstudante,name="salvar_estudante"),
    path('estudante/editar/<int:id>/',editarEstudante,name="editar_estudante"),
    path('estudante/remover/<int:id>/',excluirEstudante,name="remover_estudante"),
]
