from django.urls import path
from devpro.modulos import views

app_name = 'modulos'

urlpatterns = [
    path('<slug:slug>', views.modulo, name='modulo'),
]
