from django.shortcuts import render, get_object_or_404
from receitas.models import Receita

def index(request):
  receitas = Receita.objects.order_by('-data_receita').filter(publicado = True)
  dados = { 'receitas' : receitas }
  return render(request, 'index.html', dados)

def receita(request, id):
  receita = get_object_or_404(Receita, pk = id)
  receita_a_exibir = { 'receita' : receita }
  return render(request, 'receita.html', receita_a_exibir)

def busca(request):
  lista_receitas = Receita.objects.order_by('-data_receita').filter(publicado=True)
  if 'busca' in request.GET:
    nome_a_buscar = request.GET['busca']
    if busca:
      lista_receitas = lista_receitas.filter(nome__icontains = nome_a_buscar)

  dados = { 'receitas': lista_receitas }
  return render(request, 'busca.html', dados)

def categoria(request, categoria):
  lista_categoria = Receita.objects.order_by('-data_receita').filter(publicado=True).filter(categoria = categoria)
  categoria_a_exibir = { 'receitas': lista_categoria }
  return render(request, 'categoria.html', categoria_a_exibir)