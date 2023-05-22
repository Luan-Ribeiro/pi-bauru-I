from django.shortcuts import render, redirect

from .forms import DescartesForm
from .models import Descartes


def home(request):
    user = request.user.username
    vdescartes = Descartes.objects.all()
    return render(request, "descartes.html", {"descartes": vdescartes, "username": user})


def save(request):
    if request.method == 'POST':
        form = DescartesForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect(home)


def editar(request, id):
    user = request.user.username
    vdescartes = Descartes.objects.get(id=id)
    return render(request, "descartes-update.html", {"descartes": vdescartes, "username": user})


def update(request, id):
    if request.method == 'POST':
        form = DescartesForm(request.POST)
        if form.is_valid():
            descarte = Descartes.objects.get(id=id)
            descarte.nome = form.data.get("nome")
            descarte.tipo = form.data.get("tipo")
            descarte.quantidade = form.data.get("quantidade")
            descarte.descartador = form.data.get("descartador_documento")
            descarte.ecoponto = form.data.get("ecoponto")
            descarte.save()
    return redirect(home)


def delete(request, id):
    descarte = Descartes.objects.get(id=id)
    descarte.delete()
    return redirect(home)
