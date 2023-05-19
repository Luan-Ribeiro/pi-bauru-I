from django.contrib import admin
from django.urls import path
from .views import home, buscar, save, editar, update, delete

urlpatterns = [
    path('', home, name="home-descartadores"),
    path('buscar/<int:documento>', buscar, name="buscar-descartadores"),
    path('save/', save, name="save-descartadores"),
    path('editar/<int:documento>', editar, name="editar-descartadores"),
    path('update/<int:documento>', update, name="update-descartadores"),
    path('delete/<int:documento>', delete, name="delete-descartadores"),
]
