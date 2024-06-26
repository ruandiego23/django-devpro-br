from django.contrib.auth import get_user_model
from django.db import models


# Create your models here.
class Turma(models.Model):
    nome = models.CharField(max_length=100)
    slug = models.SlugField(max_length=120, unique=True)
    inicio = models.DateTimeField()
    fim = models.DateTimeField()
    estudantes = models.ManyToManyField(get_user_model(), through='Matricula')

    def __str__(self):
        return self.nome


class Matricula(models.Model):
    usuario = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    data_de_inscricao = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Matricula"
        verbose_name_plural = "Matriculas"
        unique_together = (('usuario', 'turma'),)
        ordering = ('turma', 'data_de_inscricao')
