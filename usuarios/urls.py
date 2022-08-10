from django.urls import path
from .  import views

urlpatterns = [
  path('cadastro', views.cadastro, name = 'cadastro'),
  path('login', views.login, name = 'login'),
  path('logout', views.logout, name = 'logout'),
  path('dashboard', views.dashboard, name = 'dashboard'),
  path('receita/enviar-receita', views.enviar_receita, name = 'enviar_receita'),
  path('deleta/<int:id>', views.deleta_receita, name = 'deleta_receita'),
  path('edita/<int:id>', views.edita_receita, name = 'edita_receita'),
  path('atualiza_receita', views.atualiza_receita, name = 'atualiza_receita')
]