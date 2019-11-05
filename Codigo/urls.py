from django.conf.urls import url
from . import views
from django.urls import path
urlpatterns = [
    url(r'^$',views.index, name='index'),
    path('cliente/', views.ClienteList.as_view()),
    path('trabajador/', views.TrabajadorList.as_view()),
]