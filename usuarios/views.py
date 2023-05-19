from django.shortcuts import render, redirect

from .forms import UsuariosForm
from .models import Usuarios


def home(request):
    vusuarios = Usuarios.objects.all()
    return render(request, "usuarios.html", {"usuarios": vusuarios})


def save(request):
    if request.method == 'POST':
        form = UsuariosForm(request.POST)
        if form.is_valid():
            form.save()
            vusuarios = Usuarios.objects.all()
            return render(request, "usuarios.html", {"usuarios": vusuarios})
    else:
        form = UsuariosForm()
    return render(request, 'usuarios.html', {'form': form})


def editar(request, id):
    vusuarios = Usuarios.objects.get(id=id)
    return render(request, "usuarios-update.html", {"usuarios": vusuarios})


def update(request, id):
    if request.method == 'POST':
        form = UsuariosForm(request.POST)
        if form.is_valid():
            usuario = Usuarios.objects.get(id=id)
            usuario.nome = form.data.get("nome")
            usuario.email = form.data.get("email")
            usuario.cargo = form.data.get("cargo")
            usuario.cpf = form.data.get("cpf")
            usuario.ecoponto = form.data.get("ecoponto")
            usuario.save()
    return redirect(home)


def delete(request, id):
    usuario = Usuarios.objects.get(id=id)
    usuario.delete()
    return redirect(home)
