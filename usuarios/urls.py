from django.contrib import admin
from django.urls import path
from .views import home, save, editar, update, delete

urlpatterns = [
    path('', home, name="home-usuarios"),
    path('save/', save, name="save-usuarios"),
    path('editar/<int:id>', editar, name="editar-usuarios"),
    path('update/<int:id>', update, name="update-usuarios"),
    path('delete/<int:id>', delete, name="delete-usuarios"),
]
