#conteúdo das páginas
from django.shortcuts import render


def index(request):
    return render(request, 'noticias/index.html')

def imagem(request):
    return render(request, 'noticias/imagem.html')
# Create your views here.
