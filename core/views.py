from django.shortcuts import render

# Create your views here.
# En tu archivo views.py
from django.views.generic import TemplateView

class AboutView(TemplateView):
    template_name = 'core/about.html' 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['descripcion'] = """
        CataldoApp es un sistema de gestión de inventario diseñado para simplificar 
        el control de productos. Con esta aplicación puedes:
        - Registrar nuevos productos con imágenes
        - Gestionar el stock disponible
        - Realizar un seguimiento de fechas de ingreso
        - Visualizar reportes detallados
        - Administrar tu inventario de forma eficiente
        
        Desarrollado con Django y Python para una experiencia robusta y escalable.
        """
        return context