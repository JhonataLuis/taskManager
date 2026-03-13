from django.shortcuts import render, redirect
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

def editar(request, id):
    task = Task.objects.get(id=id)
    return render(request, "update.html", {"task": task})

def update(request, id):
    task = Task.objects.get(id=id)

    if request.method == "POST":
        task.titulo = request.POST.get("titulo")
        task.descricao = request.POST.get("descrição")
        task.criado_em = request.POST.get("criado_em")
        task.vence_em = request.POST.get("vence_em")
        task.prioridade = request.POST.get("prioridade")
        task.concluida = request.POST.get("concluida") == "on"
        task.save()

        return redirect()


