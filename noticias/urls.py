from django.urls import path
from noticias.views import index, imagem   

#lista de endpoint 
urlpatterns = [
    path('', index, name='index'),
    path('imagem/', imagem, name='imagem')
]