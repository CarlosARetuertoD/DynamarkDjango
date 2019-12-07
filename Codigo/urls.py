from django.conf.urls import url
from . import views
from django.urls import path
urlpatterns = [
    url(r'^$',views.index, name='index'),
    path('clientes/', views.ClienteList.as_view()),
    path('cliente/<int:pk>', views.ClienteDetail.as_view()),
    path('productos/', views.ProductosList.as_view()),
    path('trabajadores/', views.TrabajadoresList.as_view()),
    path('formaspago/', views.FormaPagoList.as_view()),
    path('zona/<int:pk>/', views.ZonaList.as_view()),
    path('zonatrabajador/<int:dni>/', views.ZonaTrabajadorList.as_view()),
    path('trabajador/<int:pk>/', views.TrabajadorDetail.as_view()),
    path('pedido/<int:pk>/', views.PedidoDetail.as_view()),
    path('pedidos/', views.PedidosList.as_view()),
    path('pedidos/<int:dni>/', views.Trabajador_PedidosList.as_view()),
    path('addpedido/', views.AddPedido.as_view()),
    path('adddetallepedido/', views.AddDetallePedido.as_view()),
]