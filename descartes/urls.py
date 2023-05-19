from django.contrib import admin
from django.urls import path
from .views import home, save, editar, update, delete

urlpatterns = [
    path('', home, name="home-descartes"),
    path('save/', save, name="save-descartes"),
    path('editar/<int:id>', editar, name="editar-descartes"),
    path('update/<int:id>', update, name="update-descartes"),
    path('delete/<int:id>', delete, name="delete-descartes"),
]
