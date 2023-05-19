from django.shortcuts import render, redirect

from .forms import DescartadoresForm
from .models import Descartadores


def home(request):
    vdescartadores = Descartadores.objects.all()
    return render(request, "descartadores.html", {"descartadores": vdescartadores})


def buscar(request, documento):
    vdescartador = Descartadores.objects.get(documento=documento)
    return render(request, {"descartador": vdescartador})


def save(request):
    if request.method == 'POST':
        form = DescartadoresForm(request.POST)
        if form.is_valid():
            form.save()
            vdescartadores = Descartadores.objects.all()
            return render(request, "descartadores.html", {"descartadores": vdescartadores})
    else:
        form = DescartadoresForm()
    return render(request, 'descartadores.html', {'form': form})


def editar(request, documento):
    vdescartador = Descartadores.objects.get(documento=documento)
    return render(request, "descartadores-update.html", {"descartadores": vdescartador})


def update(request, documento):
    if request.method == 'POST':
        form = DescartadoresForm(request.POST)
        if form.is_valid():
            descartador = Descartadores.objects.get(documento=documento)
            descartador.nome = form.data.get("nome")
            descartador.email = form.data.get("email")
            descartador.documento = form.data.get("documento")
            descartador.endereco = form.data.get("endereco")
            descartador.save()
    return redirect(home)


def delete(request, documento):
    descartador = Descartadores.objects.get(documento=documento)
    descartador.delete()
    return redirect(home)
