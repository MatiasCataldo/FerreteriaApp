from django.urls import path
from CataldoApp.views import home, crear_socio, listado_de_socios

urlpatterns = [
    path('', home, name='home'),   
    path('socios/', listado_de_socios, name='listado_de_socios'),
    path('socios/crear/', crear_socio, name='crear_socio'),
]