from django.conf.urls import url
from . import views
from django.urls import path
urlpatterns = [
    url(r'^$',views.index, name='index'),
    path('clientes/', views.ClienteList.as_view()),
    path('productos/', views.ProductosList.as_view()),
    path('pedidos/', views.PedidosList.as_view()),
    path('trabajadores/', views.TrabajadoresList.as_view()),
]