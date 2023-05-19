from django.contrib import admin
from django.urls import path
from .views import home, save, editar, update, delete

urlpatterns = [
    path('', home, name="home-ecopontos"),
    path('save/', save, name="save-ecopontos"),
    path('editar/<int:id>', editar, name="editar-ecopontos"),
    path('update/<int:id>', update, name="update-ecopontos"),
    path('delete/<int:id>', delete, name="delete-ecopontos"),
]
