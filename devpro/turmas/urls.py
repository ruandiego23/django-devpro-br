from django.urls import path

from devpro.turmas import views

app_name = 'turmas'

urlpatterns = [
    path('', views.indice, name='indice'),
]
