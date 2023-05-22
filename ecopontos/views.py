from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import EcopontosForm
from .models import Ecopontos


@login_required
def home(request):
    user = request.user.username
    vecopontos = Ecopontos.objects.all()
    return render(request, "ecopontos.html", {"ecopontos": vecopontos, "username": user})


def save(request):
    if request.method == 'POST':
        form = EcopontosForm(request.POST)
        if form.is_valid():
            form.save()
            vecopontos = Ecopontos.objects.all()
            return render(request, "ecopontos.html", {"ecopontos": vecopontos})
    else:
        form = EcopontosForm()
    return render(request, 'ecopontos.html', {'form': form})


def editar(request, id):
    user = request.user.username
    vecopontos = Ecopontos.objects.get(id=id)
    return render(request, "ecopontos-update.html", {"ecopontos": vecopontos, "username": user})


def update(request, id):
    if request.method == 'POST':
        form = EcopontosForm(request.POST)
        if form.is_valid():
            ecoponto = Ecopontos.objects.get(id=id)
            ecoponto.cep = form.data.get("cep")
            ecoponto.bairro = form.data.get("bairro")
            ecoponto.endereco = form.data.get("endereco")
            ecoponto.situacao = form.data.get("situacao")
            ecoponto.save()
    return redirect(home)


def delete(request, id):
    ecoponto = Ecopontos.objects.get(id=id)
    ecoponto.delete()
    return redirect(home)
