from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required

from receitas.models import Receita

def cadastro(request):
  if request.method == 'POST':
    usuario = request.POST['username']
    nome = request.POST['name']
    email = request.POST['email']
    senha = request.POST['password']
    confirma_senha = request.POST['confirm_password']

    if not usuario.strip() or not nome.strip() :
      messages.error(request, 'Existem campos em branco')
      return redirect('cadastro')

    if senha != confirma_senha:
      messages.error(request, 'As senhas não são iguais')
      return redirect('cadastro')

    if User.objects.filter(username = usuario).exists():
      messages.error(request, 'Usuário já cadastrado')
      return redirect('cadastro')

    if User.objects.filter(email = email).exists():
      messages.error(request, 'E-mail já cadastrado')
      return redirect('cadastro')

    user = User.objects.create_user(username = usuario, first_name=nome, email=email, password=senha)
    user.save()
    return redirect('login')
  return render(request, 'usuarios/cadastro.html')

def login(request):
  if request.method == 'POST':
    usuario = request.POST['username']
    senha = request.POST['password']
    if usuario == ' ' or senha == ' ':
      messages.error(request, 'Existe(m) campo(s) em branco!')
      return redirect('login')
    if User.objects.filter(username = usuario).exists():
      user = auth.authenticate(request, username=usuario, password=senha)
      if user is not None:
        auth.login(request, user)
        messages.success(request, 'Login realizado com sucesso!')
        return redirect('dashboard')
    print(usuario, senha)
    return redirect('dashboard')
  return render(request, 'usuarios/login.html')

def logout(request):
  auth.logout(request)
  return redirect('index')

@login_required(login_url = 'login')
def dashboard(request):
    id = request.user.id
    receitas = Receita.objects.order_by('-data_receita').filter(pessoa=id)
    dados = { 'receitas' : receitas }
    return render(request, 'usuarios/dashboard.html', dados)


@login_required(login_url = 'login')
def enviar_receita(request):
  if request.method == 'POST':
    nome = request.POST['nome']
    ingredientes = request.POST['ingredientes']
    modo_preparo = request.POST['modo_preparo']
    tempo_preparo = request.POST['tempo_preparo']
    rendimento = request.POST['rendimento']
    categoria = request.POST['categoria']
    foto = request.FILES['foto']
    user = get_object_or_404(User, pk = request.user.id)
    receita = Receita.objects.create(pessoa = user, nome = nome, ingredientes = ingredientes, modo_preparo = modo_preparo, tempo_preparo = tempo_preparo, rendimento = rendimento, categoria = categoria, foto = foto)
    receita.save()
    return redirect('dashboard')
  else:
    return render(request, 'usuarios/enviar_receita.html')

def deleta_receita(request, id):
  receita = get_object_or_404(Receita, pk = id)
  receita.delete()
  return redirect('dashboard')

def edita_receita(request, id):
  receita = get_object_or_404(Receita, pk = id)
  receita_a_editar = { 'receita' : receita }
  return render(request, 'usuarios/edita_receita.html', receita_a_editar)

def atualiza_receita(request):
  if request.method == 'POST':
    id = request.POST['id']
    receita_a_atualizar = Receita.objects.get(pk = id)
    receita_a_atualizar.nome = request.POST['nome']
    receita_a_atualizar.ingredientes = request.POST['ingredientes']
    receita_a_atualizar.modo_preparo = request.POST['modo_preparo']
    receita_a_atualizar.tempo_preparo = request.POST['tempo_preparo']
    receita_a_atualizar.rendimento = request.POST['rendimento']
    receita_a_atualizar.categoria = request.POST['categoria']
    if 'foto' in request.FILES:
      receita_a_atualizar.foto = request.FILES['foto']
    receita_a_atualizar.save()
    return redirect('dashboard')