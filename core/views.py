from django.shortcuts import render


def home(request):
    return render(request, "inicio.html")


def login(request):
    return render(request, "signin.html")


def cadastro(request):
    return render(request, "signup.html")
