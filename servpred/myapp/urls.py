from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),  
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('welcome/', views.welcome, name='welcome'),
    path('menu/', views.menu, name='menu'),
    path('inicio/', views.inicio, name='inicio'),
    path('monitoreo/', views.monitoreo, name='monitoreo'),
    path('api/monitores/', views.obtener_datos_monitor, name='obtener_datos_monitor'),
    path('analisispredictivo/', views.analisispredictivo, name='analisispredictivo'),
    path('auditoria/', views.auditoria, name='auditoria'),
    path('analisisdedatos/', views.analisisdedatos, name='analisisdedatos'),
    path('recomendaciones/', views.recomendaciones, name='recomendaciones'),
    path('api/usuarios/', views.datos_administrador,  name='usuarios'),
    path('administracion/', views.administracion, name='administracion'),
    path('obtener_auditorias', views.obtener_auditorias, name='obtener_auditorias'),
    path('api/data/', views.obtener_datos_dataanalytic, name='obtener_datos_dataanalytic'),
    path('api/kpi/', views.obtener_kpi_relevantes, name='obtener_datos_kpiaanalytic'),
    path('api/servers/', views.obtener_servers, name='obtener_servers'),
    path('api/recomendations/', views.obtener_recomendations, name='obtener_recomendations'),
]












