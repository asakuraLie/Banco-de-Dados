from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from zmq import DEALER

# Create your models here.

class Usuario(models.Model):
    nickname = models.CharField(max_length=255, default='nickname')
    nascimento_usuario = models.CharField(max_length=255)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    slug = models.SlugField(max_length=255, unique=True, default='url')
    models.ForeignKey('self', on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.usuario)
    
    def get_absolute_url(self):
        return reverse("home")
    
    
class Filme(models.Model):
    nome_filme = models.CharField(max_length=255, unique=True, primary_key=True)
    sinopse = models.TextField(default='Sinopse do Filme')
    ano = models.CharField(max_length=255)
    genero = models.CharField(max_length=255)
    media = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, default='url')
    
    def __str__(self):
        return self.nome_filme
    
    def get_absolute_url(self):
        return reverse("filmes-disponiveis")

class Avaliacao(models.Model):
    titulo = models.CharField(max_length=255)
    comentario = models.TextField()
    nota = models.CharField(max_length=255)
    filme_avaliado = models.ForeignKey(Filme, on_delete=models.CASCADE, default='Nome do Filme')
    avaliador = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=255, unique=True, default='url')
    
    class Meta:
        ordering = ("-titulo",)
    
    def __str__(self):
        return self.titulo
    
    def get_absolute_url(self):
        return reverse("avaliacoes-lista")
    

class Favoritos(models.Model):
    filme_na_lista = models.ManyToManyField(Filme, 'favoritos')
    dono_lista = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=255, unique=True, default='url')
    
    def __str__(self):
        return self.dono_lista
    
    def get_absolute_url(self):
        return reverse("lista-favoritos")

class Ator(models.Model):
    nome_ator = models.CharField(max_length=255, unique=True, primary_key=True)
    nascimento_ator = models.CharField(max_length=255)
    infos_ator = models.TextField(default='Informações sobre o(a) ator(atriz)')
    filme_feito = models.ManyToManyField(Filme, 'atores')
    slug = models.SlugField(max_length=255, unique=True, default='url')
    
    def __str__(self):
        return self.nome_ator
    
    def get_absolute_url(self):
        return reverse("atores-listados")

class Diretor(models.Model):
    nome_diretor = models.CharField(max_length=255, unique=True, primary_key=True)
    nascimento_diretor = models.CharField(max_length=255)
    infos_diretor = models.TextField(default='Informações sobre o(a) diretor(a)')
    filme_dirigido = models.ManyToManyField(Filme, 'diretores')
    slug = models.SlugField(max_length=255, unique=True, default='url')
    
    def __str__(self):
        return self.nome_diretor
    
    def get_absolute_url(self):
        return reverse("diretores-listados")
    
class Produtor(models.Model):
    nome_produtor = models.CharField(max_length=255, unique=True)
    nascimento_diretor = models.CharField(max_length=255)
    filme_produzido = models.ManyToManyField(Filme, 'produtores')