from django.shortcuts import render, HttpResponse, redirect
from .models import Tarefa
from django.contrib import messages

def home(request):
    return(render(request, 'index.html'))

def lista(request):
    nova_tarefa = Tarefa()
    nova_tarefa.nome_tarefa = request.POST.get('nome')
    nova_tarefa.data = request.POST.get('data')
    nova_tarefa.hora = request.POST.get('hora')
    nova_tarefa.save()
    # exibir em uma nova página
    tarefas = {
        'tarefas': Tarefa.objects.all()
    }
    messages.success(request, 'Tarefa Cadastrada com sucesso.')
    # retornar os dados para a página de listagem de tarefas
    return render(request,'list.html', tarefas)
def tarefas(request):
    tarefas = {
        'tarefas': Tarefa.objects.all()
    }
    return(render(request,'list.html', tarefas))

def remover_tarefa(request, tarefa_id):
    tarefas = {
        'tarefas': Tarefa.objects.all()
    }
    if request.method == 'POST':
        # Busca a tarefa pelo ID
        tarefa = Tarefa.objects.get(id_tarefa=tarefa_id)
        # Remove a tarefa do banco de dados
        tarefa.delete()
        messages.success(request, 'Tarefa removida com sucesso.')
        # Redireciona para a página de lista de tarefas após a remoção
    else:
        messages.error(request, 'A tarefa não foi encontrada.')
    return redirect('lista')
