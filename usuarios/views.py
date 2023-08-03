from django.shortcuts import render, redirect
from usuarios.forms import LoginForms, CadastroForms
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages


def login(request):
    form = LoginForms()
    if request.method=='POST':
        form=LoginForms(request.POST)

        if form.is_valid():
            nome=form['nome_login'].value()
            senha=form['senha'].value()

        usuario = auth.authenticate(
            request,
            username=nome,
            password=senha
        )
        #validar info
        if usuario is not None:
            auth.login(request, usuario)
            messages.success(request, f'{nome} logado com sucesso!')
            return redirect('index')
        else:
            messages.error(request, 'Erro ao efetuar login')
            return redirect('login')



    return render(request,'usuarios/login.html', {'form': form})



def cadastro(request):

    form = CadastroForms()

    if request.method == 'POST':
        #coloca informações do formulario em um form novo   
        form = CadastroForms(request.POST)

        if form.is_valid():
            #verifica form valido e se senhas sao iguais
            if form['senha_1'].value() != form['senha_2'].value():
                messages.error(request,'Senhas não são iguais')
                return redirect('cadastro')
            #info do form
            nome=form['nome_cadastro'].value()
            email=form['email'].value()
            senha=form['senha_1'].value()
            #verifica se ja existe
            if User.objects.filter(username=nome).exists():
                messages.error(request, 'usuário já existente')
                return redirect('cadastro')
            #cria usuario
            usuario=User.objects.create_user(
                username=nome,
                email=email,
                password=senha
            )
            usuario.save()
            messages.success(request, 'Cadastr efetuado com sucesso')
            return redirect('login')

    return render(request,'usuarios/cadastro.html', {'form': form})

def logout(request):
    auth.logout(request)
    messages.success(request, 'Logout efetuado com sucesso!')
    return redirect('login')