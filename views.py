from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from .models import PlanoPainel
from .models import Equipamento
from .models import Instalacao 
from .models import orcamento
from .models import Usuario
from .models import Comentarios
from .models import Servidor
from .forms import CadastroForm
import json


def index(request):
    return render(request, 'galeria/index.html')

def empresa(request):
    return render(request, 'galeria/empresa.html')

def cadastro(request):
    return render(request, 'galeria/cadastro.html')

def login(request):
    return render(request, 'galeria/login.html')

def contato(request):
    return render(request, 'galeria/contato.html')
  
def orcamento_sucesso(request):
    return render(request, 'galeria/orcamento_sucesso.html')

def area_cliente(request):
    return render(request, 'galeria/area_cliente.html')
  
def planos(request):
    return render(request, 'galeria/planos.html')

def login_servidor(request):
    return render(request, 'galeria/login_servidor.html')

def area_servidor(request):
    return render(request, 'galeria/area_servidor.html')

def equipamento(request):
    return render(request, 'galeria/equipamento.html')
  
  
#CONTROLE DE ENVIO PARA O BANCO DE DADOS NA TABELA ORÇAMENTO:

def enviar_orcamento(request):
    if request.method == 'POST':
        # Captura os dados enviados pelo formulário
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        cep = request.POST.get('cep')
        mensagem = request.POST.get('mensagem')
        
        Orcamento = orcamento(nome=nome, email=email, telefone=telefone, cep=cep, mensagem=mensagem)
        Orcamento.save()
      
        return redirect('orcamento_sucesso')

    return JsonResponse({'status': 'erro', 'mensagem': 'Método inválido'})


#CONTROLE DE ENVIO PARA O CADASTRO NO BANCO DE DADOS NO MODELO (TABELA) Usuario. Arquivo: forms.py 

def cadastrar_usuario(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')  
    else:
        form = CadastroForm()
    
    return render(request, 'cadastro.html', {'form': form})


#CONTROLE ALERT DE SUCESSO DO CADASTRO NA PÁGINA LOGUIN:

def cadastrar(request):
  return redirect('login', cadastro_success = 'true')

#ACESSO AO MODELO (Usuario) PARA O USUÁRIO ACESSAR O SISTEMA PELA PÁGINA (login.html)


def login(request):
    error_message = None
    if request.method == 'POST':
        cpf = request.POST['cpf']
        senha = request.POST['senha']

        try:
            usuario = Usuario.objects.get(cpf=cpf, senha_cadastro=senha)
            return redirect('area_cliente')
        except ObjectDoesNotExist:
            error_message = 'CPF ou senha incorreta'

    return render(request, 'galeria/login.html', {'error_message': error_message})
  
#TRATAMENTO DE ERRO DO CADASTRO: (toda vez que o usuário errar a senha ou cpf, não aparecer aquele emaranhado de informações)
    if not usuario:
        error_message = "CPF ou senha incorretos."
        messages.error(request, error_message)
        return render(request, 'galeria/login.html')

#CONTROLE DE ENVIO PARA O BANCO DE DADOS NA TABELA COMENTARIO:
def comentar(request):
  if request.method == 'POST':
    nome = request.POST['nome']
    email = request.POST['email']
    comentario = request.POST['mensagem']

    novo_comentario = Comentarios(nome=nome, email=email, comentario=comentario)
    novo_comentario.save()

    messages.success(request, 'Comentário realizado com sucesso!')
    return redirect('index')

  return render(request, 'galeria/index.html')
    

#SISTEMA DE ENVIO DOS REGISTROS DO MODELO PlanosPainel PARA A PÁGINA PRINCIPAL (index.html)
def index(request):
    planos = PlanoPainel.objects.all()
    return render(request, 'galeria/index.html', {'planos': planos})


#SISTEMA DE REQUERIMENTO DAS IMAGENS DOS EQUIPAMENTOS NA PÁGINA PRINCIPAL (index.html) [SEM FUNCIONAR]
#def carregar_equipamentos(request):
#    equipamentos = Equipamento.objects.all()
#    return render(request, 'equipamentos_index.html', ##{'equipamentos': equipamentos, 'form': EquipamentoForm()})


#SISTEMA DE ENVIO DOS DADOS DA PÁGINA planos.html, PARA O MODELO Instalacao.


def instalacao(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        celular1 = request.POST['celular1']
        celular2 = request.POST['celular2']
        telefone = request.POST['telefone']
        cidade = request.POST['cidade']
        estado = request.POST['estado']
        cep = request.POST['cep']
        bairro = request.POST['bairro']
        endereco = request.POST['endereco']
        numero = request.POST['numero']
        complemento = request.POST['complemento']
        observacao = request.POST['observacao']
        cupom = request.POST['cupom']
        cpf = request.POST['cpf']
      

        registro = Instalacao(nome=nome, email=email, celular1=celular1, celular2=celular2, telefone=telefone, cidade=cidade, estado=estado, cep=cep, bairro=bairro, endereco=endereco, numero=numero, complemento=complemento, observacao=observacao, cupom=cupom, cpf=cpf)
        registro.save()

        messages.success(request, 'Solicitação de instalação enviada com sucesso!')
        return redirect('/index/')

    return render(request, 'galeria/planos.html')
  
#ACESSO AO MODELO Servidor PARA O SERVIDOR ACESSAR O SISTEMA PELA PÁGINA (login_servidor.html)

def login_servidor(request):
  if request.method == 'POST':
    cpf_servidor = request.POST['cpf_servidor']
    senha_servidor = request.POST['senha-servidor']

    try:
      servidor = Servidor.objects.get(cpf = cpf_servidor, senha = senha_servidor)
      return redirect('area_servidor')
    except ObjectDoesNotExist:
      error_message = 'CPF ou SENHA incorreta'
      return render(request, 'login_servidor.html', {'error_message': error_message})

  return render(request, 'galeria/login_servidor.html')


#FIREBASE EM CONJUNTO COM REACT-NATIVE:

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from firebase_admin import auth

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=100)  

# Sinal para registrar o cliente no Firebase quando um novo cliente for criado
@receiver(post_save, sender=Cliente)
def registrar_cliente_no_firebase(sender, instance, **kwargs):
    user = auth.create_user(
        email=instance.email,
        password=instance.senha,
        display_name=instance.nome
    )
