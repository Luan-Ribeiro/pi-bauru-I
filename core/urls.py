from django.contrib import admin
from django.urls import path, include

from core.views import home, login, cadastro

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', home),
    path('login/', login),
    path('cadastro/', cadastro),
    path('ecopontos/', include('ecopontos.urls')),
    path('usuarios/', include('usuarios.urls')),
    path('descartadores/', include('descartadores.urls')),
    path('descartes/', include('descartes.urls'))
]
