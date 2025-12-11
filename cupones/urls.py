from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # La portada
    path('cupones/', views.cupones_view, name='cupones'), # Página de cupones separada
    path('api/cupones/', views.lista_cupones, name='lista_cupones'), # Datos JSON
    path('api/canjear/<int:id>/', views.canjear_cupon, name='canjear_cupon'), # Acción
    path('api/fotos/', views.lista_fotos_cronologicas, name='lista_fotos'),
]