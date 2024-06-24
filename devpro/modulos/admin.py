from django.contrib import admin

from devpro.modulos.models import Modulo


# Register your models here.

@admin.register(Modulo)
class ModuloAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'publico', 'descricao', 'criado_em', 'modificado_em')
    prepopulated_fields = {'slug': ('titulo',)}
    search_fields = ('titulo',)
