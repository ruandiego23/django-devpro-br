from django.contrib import admin

from devpro.turmas.models import Turma


# Register your models here.
class MatriculaInline(admin.TabularInline):
    model = Turma.estudantes.through
    extra = 1
    readonly_fields = ('data_de_inscricao',)
    autocomplete_fields = ('usuario',)


@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin):
    inlines = [MatriculaInline]
    list_display = ('nome', 'slug', 'inicio', 'fim')
    search_fields = ('nome',)
    prepopulated_fields = {'slug': ('nome',)}
    ordering = ('-inicio',)
