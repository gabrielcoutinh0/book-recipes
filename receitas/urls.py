from django.urls import path
from .  import views

urlpatterns = [
  path('', views.index, name = 'index'),
  path('<int:id>', views.receita, name = 'receita'),
  path('busca', views.busca, name = 'busca'),
  path('categoria/<slug:categoria>', views.categoria, name = 'categoria'),
]