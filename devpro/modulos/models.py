from django.db import models
from django.urls import reverse


# Create your models here.


class Modulo(models.Model):
    titulo = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, max_length=125)
    publico = models.TextField(max_length=250)
    descricao = models.TextField(max_length=500)
    criado_em = models.DateTimeField(auto_now_add=True)
    modificado_em = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-criado_em',)
        verbose_name = 'Modulo'
        verbose_name_plural = 'Modulos'

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('modulos:modulo', kwargs={'slug': self.slug})
