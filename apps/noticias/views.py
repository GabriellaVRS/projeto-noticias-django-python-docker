#conteúdo das páginas
from django.shortcuts import render, get_object_or_404, redirect
from apps.noticias.models import Fotografia
from django.contrib import messages


def index(request):
    if not request.user.is_authenticated:
        messages.error(request,'Usuário não logado')
        return redirect('login')

    fotografias = Fotografia.objects.order_by('data_fotografia').filter(publicada=True)
    return render(request, 'noticias/index.html', {'cards': fotografias})

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)    
    return render(request, 'noticias/imagem.html', {'fotografia': fotografia})

def buscar(request):
    if not request.user.is_authenticated:
        messages.error(request,'Usuário não logado')
        return redirect('login')

    fotografias = Fotografia.objects.order_by('data_fotografia').filter(publicada=True)

    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar)
            
    return render(request, 'noticias/buscar.html', {'cards': fotografias})
# Create your view:s here.

def nova_imagem(request):
    return render(request, 'noticias/nova_imagem.html')

def editar_imagem(request):
    pass

def deletar_imagem(request):
    pass
