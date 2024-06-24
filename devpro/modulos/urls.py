from django.urls import path
from devpro.modulos import views

app_name = 'modulos'

urlpatterns = [
    path('<slug:slug>', views.modulo_aulas, name='modulo'),
    path('aulas/<slug:slug>', views.aula, name='aula'),
]
