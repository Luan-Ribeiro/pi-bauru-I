from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from core.views import home, user_register, user_login, page_register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='user_login'),
    path('login/verify', user_login, name="user_login"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('inicio/', home),
    path('registro/', page_register, name="page_register"),
    path('registro/save', user_register, name="user_register"),
    path('ecopontos/', include('ecopontos.urls')),
    path('usuarios/', include('usuarios.urls')),
    path('descartadores/', include('descartadores.urls')),
    path('descartes/', include('descartes.urls'))
]
