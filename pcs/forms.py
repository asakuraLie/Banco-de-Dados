from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import *
from django.contrib.auth.models import User
from django.db import models

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('nickname', 'nascimento_usuario', 'usuario', 'slug')
        
        widgets = {
            'nickname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Coloque aqui o seu nickname'}),
            'nascimento_usuario': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Coloque aqui a data do seu nascimento'}), 
            'usuario': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Coloque aqui quem é você'}),
            'slug': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Coloque aqui um "slug" (entenda como negócio em cima do site)'}),
        }

class AvaliacaoForm(forms.ModelForm):
    class Meta:
        model = Avaliacao
        fields = ('titulo', 'filme_avaliado', 'slug', 'avaliador', 'nota', 'comentario')
        
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Coloque aqui o título da sua avaliação'}),
            'filme_avaliado': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Coloque aqui o filme avaliado'}),
            'slug': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Coloque aqui um "slug" (entenda como negócio em cima do site)'}),
            'avaliador': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Coloque aqui quem é você'}),
            'nota': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Coloque aqui a nota do filme'}),
            'comentario': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Coloque aqui o seu comentário do filme'}),
        }
        
class EditAvaliacaoForm(forms.ModelForm):
    class Meta:
        model = Avaliacao
        fields = ('titulo', 'filme_avaliado', 'avaliador', 'nota', 'comentario')
        
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Coloque aqui o título da sua avaliação'}),
            'filme_avaliado': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Coloque aqui o filme avaliado'}),
            'avaliador': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Coloque aqui quem é você'}),
            'nota': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Coloque aqui a nota do filme'}),
            'comentario': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Coloque aqui o seu comentário do filme'}),
        }
        
class FilmeForm(forms.ModelForm):
    class Meta:
        model = Filme
        fields = ('nome_filme', 'ano', 'sinopse', 'genero', 'media', 'slug')
        
        widgets = {
            'nome_filme': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Coloque aqui o nome do filme'}), 
            'ano': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Coloque aqui o ano do filme'}), 
            'sinopse': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Coloque aqui a sinopse do filme'}),
            'genero': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Coloque aqui o gênero do filme'}),
            'media': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Coloque aqui onde é possível assitir o filme'}),
            'slug': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Coloque aqui um "slug" (entenda como negócio em cima do site)'}),
        }
        
class EditFilmeForm(forms.ModelForm):
    class Meta:
        model = Filme
        fields = ('nome_filme', 'ano', 'sinopse', 'genero', 'media', 'slug')
        
        widgets = {
            'nome_filme': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Coloque aqui o nome do filme'}), 
            'ano': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Coloque aqui o ano do filme'}), 
            'sinopse': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Coloque aqui a sinopse do filme'}),
            'genero': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Coloque aqui o gênero do filme'}),
            'media': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Coloque aqui onde é possível assitir o filme'}),
            'slug': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Coloque aqui um "slug" (entenda como negócio em cima do site)'}),
        }
        
class AtorForm(forms.ModelForm):
    class Meta:
        model = Ator
        fields = ('nome_ator', 'nascimento_ator', 'infos_ator', 'filme_feito', 'slug')
        
        widgets = {
            'nome_ator': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Coloque aqui o nome do ator/atriz'}),  
            'nascimento_ator': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Coloque aqui o nascimento do ator/atriz'}),
            'infos_ator': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Coloque aqui o seu comentário do filme'}),  
            'filme_feito': forms.SelectMultiple(attrs={'class': 'form-control', 'placeholder': 'Coloque aqui o(s) filme(s) feito(s)'}),  
            'slug': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Coloque aqui um "slug" (entenda como negócio em cima do site)'}), 
        }
        
class EditAtorForm(forms.ModelForm):
    class Meta:
        model = Ator
        fields = ('nome_ator', 'nascimento_ator', 'infos_ator', 'filme_feito', 'slug')
        
        widgets = {
            'nome_ator': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Coloque aqui o nome do ator/atriz'}),  
            'nascimento_ator': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Coloque aqui o nascimento do ator/atriz'}),
            'infos_ator': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Coloque aqui o seu comentário do filme'}),  
            'filme_feito': forms.SelectMultiple(attrs={'class': 'form-control', 'placeholder': 'Coloque aqui o(s) filme(s) feito(s)'}),  
            'slug': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Coloque aqui um "slug" (entenda como negócio em cima do site)'}), 
        }
        
class DiretorForm(forms.ModelForm):
    class Meta:
        model = Diretor
        fields = ('nome_diretor', 'nascimento_diretor', 'infos_diretor', 'filme_dirigido', 'slug')
        
        widgets = {
            'nome_diretor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Coloque aqui o nome do diretor/diretora'}), 
            'nascimento_diretor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Coloque aqui o nome do diretor'}),
            'infos_diretor': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Coloque aqui o seu comentário do filme'}),  
            'filme_dirigido': forms.SelectMultiple(attrs={'class': 'form-control', 'placeholder': 'Coloque aqui o(s) filme(s) feito(s)'}),  
            'slug': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Coloque aqui um "slug" (entenda como negócio em cima do site)'}), 
        }
        
class EditDiretorForm(forms.ModelForm):
    class Meta:
        model = Diretor
        fields = ('nome_diretor', 'nascimento_diretor', 'infos_diretor', 'filme_dirigido', 'slug')
        
        widgets = {
            'nome_diretor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Coloque aqui o nome do diretor/diretora'}), 
            'nascimento_diretor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Coloque aqui o nome do diretor'}),
            'infos_diretor': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Coloque aqui o seu comentário do filme'}),  
            'filme_dirigido': forms.SelectMultiple(attrs={'class': 'form-control', 'placeholder': 'Coloque aqui o(s) filme(s) feito(s)'}),  
            'slug': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Coloque aqui um "slug" (entenda como negócio em cima do site)'}), 
        }
        
class FavoritoForm(forms.ModelForm):
    class Meta:
        model = Favoritos
        fields = ('dono_lista', 'filme_na_lista', 'slug')
        
        widgets = {
            'filme_na_lista': forms.SelectMultiple(attrs={'class': 'form-control', 'placeholder': 'Coloque aqui o nome do filme favorito'}),
            'dono_lista': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Coloque aqui o nome do dono da lista'}),
            'slug': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Coloque aqui um "slug" (entenda como negócio em cima do site)'}), 
        }
        
class EditFavoritoForm(forms.ModelForm):
    class Meta:
        model = Favoritos
        fields = ('filme_na_lista',)
        
        widgets = {
            'filme_na_lista': forms.SelectMultiple(attrs={'class': 'form-control', 'placeholder': 'Coloque aqui o nome do filme favorito'}),
        }
        
class ProfileForm(UserChangeForm):
    email = forms.EmailField(max_length=100, widget=forms.EmailInput(attrs={'class': 'form=control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')