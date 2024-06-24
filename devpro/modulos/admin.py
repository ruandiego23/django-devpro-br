from django.contrib import admin

from devpro.modulos.models import Modulo, Aula


# Register your models here.

@admin.register(Modulo)
class ModuloAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'slug', 'publico', 'descricao', 'criado_em', 'modificado_em')
    prepopulated_fields = {'slug': ('titulo',)}
    search_fields = ('titulo',)


@admin.register(Aula)
class AulaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'slug', 'criado_em', 'modificado_em')
    prepopulated_fields = {'slug': ('titulo',)}
    search_fields = ('titulo',)
    list_filter = ('modulo',)
