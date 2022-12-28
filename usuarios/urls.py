from django.urls import path
from . import views

urlpatterns =[
    path('list/', views.usuariolist, name = 'usuario_list'),
]
