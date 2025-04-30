from django.shortcuts import render, redirect
from ProductosApp.forms import CreacionProducto 
from ProductosApp.models import Producto
from django.contrib import messages 
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.
def inicio(request):
    return render(request, 'productos/inicio.html') 


@login_required
def crear_producto(request):
    if request.method == 'POST':
        formulario = CreacionProducto(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            producto = Producto(nombreProducto=info.get('nombreProducto'), 
                        idProducto=info.get('idProducto'), 
                        stock=info.get('stock'), 
                        fechaIngreso=info.get('fechaIngreso'))
            producto.save()
            messages.success(request, 'Producto creado con éxito!')
            return redirect('listado_de_productos')
    else:
        formulario = CreacionProducto()     
    return render(request, 'productos/crear_producto.html', {'formulario': formulario})


def listado_de_productos(request):
    busqueda = request.GET.get('busqueda')
    if busqueda:
        productos = Producto.objects.filter(nombreProducto__icontains=busqueda)
    else:
        productos = Producto.objects.all()
    cantidad_productos = productos.count()
    return render(request, 'productos/listado_de_productos.html', {
        'productos': productos,
        'cantidad_productos': cantidad_productos,
    })


class VistaDetalleProducto(DetailView):
    model = Producto
    template_name = "productos/detalle_producto.html"


class VistaModificarProducto(LoginRequiredMixin, UpdateView):
    model = Producto
    template_name = "productos/modificar_producto.html"
    fields = ["nombreProducto", "idProducto", "stock", "fechaIngreso"]
    success_url = reverse_lazy('listado_de_productos')

    def form_valid(self, form):
        messages.success(self.request, "¡Producto modificado con éxito!")
        return super().form_valid(form)


class VistaEliminarProducto(LoginRequiredMixin, DeleteView):
    model = Producto
    template_name = "productos/eliminar_producto.html"
    success_url = reverse_lazy('listado_de_productos')

    def form_valid(self, form):
        messages.success(self.request, "¡Producto eliminado con éxito!")
        return super().form_valid(form)