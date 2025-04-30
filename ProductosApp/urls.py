from django.urls import path
from ProductosApp.views import inicio, crear_producto, listado_de_productos, VistaDetalleProducto, VistaModificarProducto, VistaEliminarProducto

urlpatterns = [
    path('', inicio, name='inicio'),   
    path('productos/', listado_de_productos, name='listado_de_productos'),
    path('productos/crear/', crear_producto, name='crear_producto'),
    path('productos/<int:pk>/', VistaDetalleProducto.as_view(), name='detalle_producto'),
    path('productos/<int:pk>/modificar/', VistaModificarProducto.as_view(), name='modificar_producto'),
    path('productos/<int:pk>/eliminar/', VistaEliminarProducto.as_view(), name='eliminar_producto'),   
]