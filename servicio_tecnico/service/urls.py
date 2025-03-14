from django.urls import path
from service import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login_user/', views.login_user, name='login'),
    path('iniciar-sesion/', views.iniciar_sesion, name='sesion'),
    path('registro-usuario/', views.registrar_usuario, name='registro_usuario'),
    path('cerrar-sesion/', views.logout_user, name='salir'),
    path('panel-de-control/', views.panel_de_control, name='panelPC'),
    path('datos-usuario/', views.datos_usuario, name='datos_usuario'),
]