from django.conf.urls import url
from . import views
from django.urls import path
urlpatterns = [
    url(r'^$',views.index, name='index'),
    path('cliente/', views.ClienteList.as_view()),
    path('trabajador/', views.TrabajadorList.as_view()),
    path('categoria/', views.CategoriaList.as_view()),
    path('producto/', views.ProductoList.as_view()),
    path('detalle/', views.ProductoList.as_view()),
    path('pedido/', views.CabeceraList.as_view()),
]