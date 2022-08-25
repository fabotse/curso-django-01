from multiprocessing import context
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *
from chamados.models import *

# Create your views here.
def index(request):
    colaboradores = Colaborador.objects.all()
    
    chamados = Chamado.objects.all().order_by('-id')[:5]
    chamados_finalizados = Chamado.objects.filter(status='Finalizado')
    chamados_abertos = Chamado.objects.filter(status='Aberto')

    #Total
    total_chamados_finalizados = chamados_finalizados.count()
    total_chamados = Chamado.objects.count()
    total_chamados_abertos = chamados_abertos.count()
    
    context = { 'colaboradores' : colaboradores, 'chamados' : chamados, 'total_chamados' : total_chamados, 
    'total_chamados_finalizados' : total_chamados_finalizados, 'total_chamados_abertos' : total_chamados_abertos}

    return render(request, 'dashboard.html', context)

def colaborador(request, pk):
    colaborador = Colaborador.objects.get(id=pk)
    chamados = colaborador.chamado_set.order_by('-data_criacao')
    total_chamados = chamados.count()

    context = {"colaborador" : colaborador, "chamados" : chamados, 'total_chamados' : total_chamados}

    return render(request, 'colaborador.html', context)


def criarChamado(request,pk):
    colaborador = Colaborador.objects.get(id=pk)
    form = ChamadoForm(initial={'colaborador' : colaborador })

    if request.method == 'POST':
        form = ChamadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form' : form}
    return render(request, 'chamado_form.html', context)

def updateChamado(request, pk):
    chamado = Chamado.objects.get(id=pk)
    form = ChamadoForm(instance=chamado)

    if request.method == 'POST':
        form = ChamadoForm(request.POST, instance=chamado)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form' : form}
    return render(request, 'chamado_form.html', context)


def deletarChamado(request, pk):
    chamado = Chamado.objects.get(id=pk) 

    if request.method == 'POST':
        chamado.delete()
        return redirect('/')

    context = {'chamado' : chamado}
    return render(request, 'delete.html' , context)