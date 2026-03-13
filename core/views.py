from django.shortcuts import render
from .models import Task

# Create your views here.
def home(request):
    tarefas = Task.objects.all()
    return render(request, "index.html", {"tarefas": tarefas})