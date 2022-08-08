from django.contrib import admin
from .models import Receita

class listandoReceitas(admin.ModelAdmin):
  list_display = ('id', 'nome', 'categoria', 'publicado')
  list_display_links = ('id', 'nome')
  search_fields = ('nome',)
  list_filter = ('categoria',)
  list_editable = ('publicado',)

admin.site.register(Receita, listandoReceitas)