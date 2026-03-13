from django.db import models

# Create your models here.
class Task(models.Model):
    PRIORITY_CHOICES = [
        (1, 'Baixa'),
        (2, 'Média'),
        (3, 'Alta'),
    ]

    titulo = models.CharField(max_length=200)
    descricao = models.CharField(blank=True)

    # Datas importantes
    criado_em = models.DateTimeField(auto_now_add=True)
    vence_em = models.DateTimeField(null=True, blank=True)

    # Status
    concluida = models.BooleanField(default=False)
    prioridade = models.IntegerField(choices=PRIORITY_CHOICES, default=2)

    def __srt__(self):
        return self.titulo, self.descricao, self.criado_em, self.vence_em, self.concluida, self.prioridade

class Meta:
    ordering = ['-prioridade', 'vence_em']