from django.shortcuts import render
from .models import Usuarios

# Create your views here.
def usuariolist(request):
    get_usuario = Usuarios.objects.all()

    data = {
        'get_usuario': get_usuario
    }
    return render(request, 'usuariolist.html', data)
