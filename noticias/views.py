#conteúdo das páginas
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>Notícias</h1>')

# Create your views here.
