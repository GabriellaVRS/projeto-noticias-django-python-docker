from django.db import models

# Create your models here.
class Escritor(models.Model):
    nome = models.CharField(max_length=50)
    #uf = models.CharField(max_length=2, verbose_name='UF')


    def __str__(self):
        return self.nome
    
