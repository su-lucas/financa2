from django.urls import path
from . import views

urlpatterns = [
    path('categorias/', views.listar_categorias, name='listar_categorias'),
]