from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def do_login(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST.get('usuario'), password=request.POST.get('senha'))
        if user is not None:
            login(request, user)
            return redirect('/index')
    return render(request, 'login.html')

def do_logout(request):
	logout(request)
	return render(request, 'login.html')

@login_required
def index(request):
    return render(request, 'index.html', context={})

@login_required
def listafuncionarios(request):
    lista_funcionarios= Funcionario.objects.all()
    return render(request, 'lista_funcionario.html', context={'lista_funcionarios':lista_funcionarios})

@login_required
def cadastrarfuncionarios(request):
    return render(request, 'add_funcionario.html',context=None)

@login_required
def editarfuncionarios(request,id):
    funcionario= Funcionario.objects.get(pk=id)
    return render(request, 'add_funcionario.html',context={'funcionario':funcionario}) #tem que ser o mesmo nome no formulário

@login_required
def removerfuncionarios(request, id):
    funcionario= Funcionario.objects.get(id=id)
    funcionario.delete()
    return redirect('/funcionario')

@login_required
def salvarfuncionarios(request):
    nome= request.POST.get('nome_funcionario')
    sobrenome= request.POST.get('sobrenome_funcionario')
    cpf= request.POST.get('cpf_funcionario')
    tempo_de_servico= request.POST.get('tempo_funcionario')
    remuneracao= request.POST.get('remuneracao_funcionario')
    id_funcionario= request.POST.get('id_funcionario')

    if id_funcionario:
        funcionario= Funcionario.objects.get(pk=id_funcionario)
    else:
        funcionario= Funcionario()

    funcionario.nome= nome
    funcionario.sobrenome= sobrenome
    funcionario.cpf= cpf
    funcionario.tempo_de_servico= tempo_de_servico
    funcionario.remuneracao= remuneracao
    funcionario.save()
    return redirect('/funcionario')
@login_required
def lista_veiculos(request):
    lista_veiculos = Veiculo.objects.all()
    return render(request, 'lista_veiculo.html', context={'lista_veiculos':lista_veiculos})
@login_required
def criar_veiculo(request):
    return render(request, 'add_veiculo.html', context=None)
@login_required
def salvar_veiculo(request):
    user = User.objects.get(username=request.user)
    marca = request.POST.get('marca')
    modelo = request.POST.get('modelo')
    tipo = request.POST.get('tipo')
    combustivel = request.POST.get('combustivel')
    placa = request.POST.get('placa')
    chassi = request.POST.get('chassi')
    ano = request.POST.get('ano')
    capacidade = request.POST.get('capacidade')
    id_veiculo= request.POST.get('id_veiculo')
    if id_veiculo:
        veiculo= Veiculo.objects.get(pk=id_veiculo)
    else:
        veiculo= Veiculo()
    veiculo.marca= marca
    veiculo.modelo= modelo
    veiculo.tipo= tipo
    veiculo.combustivel= combustivel
    veiculo.placa= placa
    veiculo.chassi= chassi
    veiculo.ano= ano
    veiculo.capacidade= capacidade
    veiculo.save()
    return redirect('/veiculo')
@login_required
def editar_veiculos(request,id):
    usuarios = User.objects.all()
    veiculo= Veiculo.objects.get(pk=id)
    return render(request, 'add_veiculo.html', context={'veiculo': veiculo,'usuarios':usuarios})
@login_required
def remover_veiculos(request,id):
    veiculo = Veiculo.objects.get(id=id)
    veiculo.delete()
    return redirect('/veiculo')
@login_required
def listaAtendimento(request):
    lista_atendimento = Atendimento.objects.all()
    return render(request, 'lista_atendimento.html', context={'lista_atendimento': lista_atendimento})
@login_required
def cadastrarAtendimento(request):
    funcionarios = Funcionario.objects.all()
    veiculos = Veiculo.objects.all()

    context = { 'funcionarios': funcionarios, 'veiculos': veiculos}

    return render(request, 'add_atendimento.html',context)
@login_required
def salvarAtendimento(request):
    funcionario = request.POST.get('motorista_atendimento')
    veiculo = request.POST.get('veiculo_atendimento')
    destino = request.POST.get('destino')
    observacao = request.POST.get('observacao')
    id_atendimento= request.POST.get('id_atendimento')
    if id_atendimento:
        atendimento= Atendimento.objects.get(pk=id_atendimento)
    else:
        atendimento= Atendimento()
    atendimento.motorista_id=funcionario
    atendimento.veiculo_id=veiculo
    atendimento.destino=destino
    atendimento.observacao=observacao
    atendimento.save()
    return redirect('/atendimento')
@login_required
def editarAtendimento(request,id):
    funcionarios = Funcionario.objects.all()
    veiculos = Veiculo.objects.all()
    atendimento= Atendimento.objects.get(pk=id)
    context = {
        "atendimento":atendimento,
        "veiculos":veiculos,
        "funcionarios":funcionarios,
    }
    return render(request,'add_atendimento.html',context)
@login_required
def removerAtendimento(request,id):
    atendimento= Atendimento.objects.get(id=id)
    atendimento.delete()
    return redirect('/atendimento')

@login_required
def listaEstudante(request):
    estudantes= Estudante.objects.all()
    return render(request,"lista_estudante.html",context={'estudantes': estudantes})

def cadastrarEstudante(request):
    return render(request,"add_estudante.html",context=None)

def salvarEstudante(request):
    nome= request.POST.get('nome')
    matricula = request.POST.get('matricula')
    cpf = request.POST.get('cpf')
    rg = request.POST.get('rg')
    curso = request.POST.get('curso')
    faculdade = request.POST.get('faculdade')

    id_estudante = request.POST.get('id_estudante')
    if id_estudante:
        estudante = Estudante.objects.get(pk=id_estudante)
    else:
        estudante= Estudante()

    estudante.nome=nome
    estudante.matricula=matricula
    estudante.cpf=cpf
    estudante.rg=rg
    estudante.curso=curso
    estudante.faculdade=faculdade
    estudante.save()
    return redirect('/estudante')

def editarEstudante(request,id):
    estudante= Estudante.objects.get(pk=id)
    return render(request,"add_estudante.html",context={'estudante':estudante})

def excluirEstudante(request,id):
    estudante = Estudante.objects.get(id=id)
    estudante.delete()
    return redirect('/estudante')
