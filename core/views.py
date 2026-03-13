from django.shortcuts import render
from .models import Task

# Create your views here.
def home(request):
    tarefas = Task.objects.all()
    return render(request, "index.html", {"tarefas": tarefas})

def salvar(request):
    titulo = request.POST.get("titulo")
    descricao = request.POST.get("descricao")
    criado_em = request.POST.get("criado_em")
    vence_em = request.POST.get("vence_em")
    concluida = request.POST.get("concluida") == "on" # Checkbox retorna 'on' quando marcado
    prioridade = request.POST.get("prioridade")
    Task.objects.create(
        titulo=titulo, 
        descricao=descricao,
        criado_em=criado_em,
        vence_em=vence_em,
        concluida=concluida,
        prioridade=prioridade
        )
    tarefas = Task.objects.all()
    return render(request, "index.html", {"tarefas": tarefas})


