from django.urls import path
from noticias.views import index

#lista de endpoint 
urlpatterns = [
    path('', index)
]