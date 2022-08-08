from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth

from receitas.models import Receita

def cadastro(request):
  if request.method == 'POST':
    usuario = request.POST['username']
    nome = request.POST['name']
    email = request.POST['email']
    senha = request.POST['password']
    confirma_senha = request.POST['confirm_password']

    if not usuario.strip() or not nome.strip() :
      print('Existem campos em branco')
      return redirect('cadastro')

    if senha != confirma_senha:
      print('As senhas não são iguais')
      return redirect('cadastro')

    if User.objects.filter(username = usuario).exists():
      print('Usuário já cadastrado')
      return redirect('cadastro')

    if User.objects.filter(email = email).exists():
      print('E-mail já cadastrado')
      return redirect('cadastro')

    user = User.objects.create_user(username = usuario, first_name=nome, email=email, password=senha)
    user.save()
    return redirect('login')
  return render(request, 'usuarios/cadastro.html')

def login(request):
  if request.method == 'POST':
    usuario = request.POST['username']
    senha = request.POST['password']
    if usuario == '' or senha == '':
      print('Existe(m) campo(s) em branco!')
      return redirect('login')
    if User.objects.filter(username = usuario).exists():
      user = auth.authenticate(request, username=usuario, password=senha)
      if user is not None:
        auth.login(request, user)
        print('Login realizado com sucesso!')
        return redirect('dashboard')
    print(usuario, senha)
    return redirect('dashboard')
  return render(request, 'usuarios/login.html')

def logout(request):
  auth.logout(request)
  return redirect('index')

def dashboard(request):
  if request.user.is_authenticated:
    id = request.user.id
    receitas = Receita.objects.order_by('-data_receita').filter(pessoa=id)
    dados = { 'receitas' : receitas }
    return render(request, 'usuarios/dashboard.html', dados)
  else:
    return redirect('index')

def enviar_receita(request):
  if request.method == 'POST':
    nome = request.POST['nome']
    ingredientes = request.POST['ingredientes']
    modo_preparo = request.POST['modo_preparo']
    tempo_preparo = request.POST['tempo_preparo']
    rendimento = request.POST['rendimento']
    categoria = request.POST['categoria']
    foto = request.FILES['foto']
    user = get_object_or_404(User, pk=request.user.id)
    receita = Receita.objects.create(pessoa=user, nome=nome, ingredientes=ingredientes, modo_preparo=modo_preparo, tempo_preparo=tempo_preparo, rendimento=rendimento, categoria=categoria, foto=foto)
    receita.save()
    return redirect('dashboard')
  else:
    if request.user.is_authenticated:
      return render(request, 'usuarios/enviar_receita.html')
    else:
      return redirect('login')