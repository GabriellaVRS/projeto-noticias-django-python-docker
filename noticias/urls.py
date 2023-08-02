from django.urls import path
from noticias.views import index, imagem, buscar 

#lista de endpoint 
urlpatterns = [
    path('', index, name='index'),
    path('imagem/<int:foto_id>', imagem, name='imagem'),
    path('buscar', buscar, name='buscar'),
]