from django.urls import path

from devpro.base import views

app_name = 'base'

urlpatterns = [
    path('', views.home, name='home'),
    path('inscrever/', views.sign_up, name='sign_up'),
]
