from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('agregar/', views.agregar_partido, name='agregar_partido'),
    path('editar/<int:id_partido>/', views.editar_partido, name='editar_partido'),
    path('eliminar/<int:id_partido>/', views.eliminar_partido, name='eliminar_partido'),
]