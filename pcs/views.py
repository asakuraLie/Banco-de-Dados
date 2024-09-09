from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from . models import *
from .forms import *

#def home(request):
#    return render(request, 'home.html', {})

class UsuarioDetail(DetailView):
    model = Usuario
    template_name = 'usuario_detalhes.html'

class UsuarioCriar(CreateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = 'adicionar_usuario.html'

class HomeView(ListView):
    model = Avaliacao
    template_name = 'home.html'
    
    def getInfos(request):
        
        favoritos = Favoritos.objects.all()
        filmes = Filme.objects.all()
        usuario = Usuario.objects.all()
        
        return render(request, 'home.html')

class AvaliacoesView(ListView):
    model = Avaliacao
    template_name = 'avaliacoes_lista.html'
    ordering = ['filme_avaliado']
    
    def getInfos(request):
        
        favoritos = Favoritos.objects.all()
        filmes = Filme.objects.all()
        usuario = Usuario.objects.all()
        
        return render(request, 'favoritos_lista.html')
    
class FavoritosView(ListView):
    model = Favoritos
    template_name = 'favoritos_lista.html'
    
    def getInfos(request):
        
        favoritos = Favoritos.objects.all()
        filmes = Filme.objects.all()
        usuario = Usuario.objects.all()
        
        return render(request, 'favoritos_lista.html')
    
class FavoritosDetail(DetailView):
    model = Favoritos
    template_name = 'favoritos_detalhes.html'
    
    def getInfos(request):
        
        favoritos = Favoritos.objects.all()
        filmes = Filme.objects.all()
        usuario = Usuario.objects.all()
        
        return render(request, 'favoritos_detalhes.html')
    
class FilmeView(ListView):
    model = Filme
    template_name = 'filme_lista.html'
    
class AtoresView(ListView):
    model = Ator
    template_name = 'atores_lista.html'
    
class DiretoresView(ListView):
    model = Diretor
    template_name = 'diretores_lista.html'
    
class AvalicoesDetail(DetailView):
    model = Avaliacao
    template_name = 'avaliacoes_detalhes.html'
    
class FilmeDetail(DetailView):
    model = Filme
    template_name = 'filmes_detalhes.html'
    
    def getInfos(request):
        
        diretores = Diretor.objects.all()
        atores = Ator.objects.all()
        filmes = Filme.objects.all()
        
        return render(request, 'filmes_detalhes.html')
    
class AtorDetail(DetailView):
    model = Ator
    template_name = 'atores_detalhes.html'
    
    def getFilmes(request):
        
        atores = Ator.objects.all().order_by('-nome_ator')
        filmes = Filme.objects.all()
        
        return render(request, 'atores_detalhes.html')
    
class DiretorDetail(DetailView):
    model = Diretor
    template_name = 'diretores_detalhes.html'
    
    def getFilmes(request):
        
        diretores = Diretor.objects.all().order_by('-nome_ator')
        filmes = Filme.objects.all()
        
        return render(request, 'diretores_detalhes.html')
    
class AvaliacoesCriar(CreateView):
    model = Avaliacao
    form_class = AvaliacaoForm
    template_name = 'adicionar_avaliacao.html'
    #fields = '__all__'
    #fields = ('titulo', 'filme_avaliado', 'comentario', 'nota')
    
class AvaliacoesEditar(UpdateView):
    model = Avaliacao
    form_class = EditAvaliacaoForm
    template_name = 'avaliacoes_editar.html'

def AvaliacoesPorFilme(request, fms):
    avaliacoes = Avaliacao.objects.filter(filme_avaliado=fms)
    return render(request, 'avaliacoes_por_filme.html', {'fms': fms, 'avaliacoes': avaliacoes})
    #fields = '__all__'
    #fields = ('titulo', 'filme_avaliado', 'comentario', 'nota')
    
def AvaliacoesPorUsuario(request, us):
    avaliacoes = Avaliacao.objects.filter(avaliador=us)
    return render(request, 'avaliacoes_por_usuario.html', {'us': us, 'avaliacoes': avaliacoes})
    #fields = '__all__'
    #fields = ('titulo', 'filme_avaliado', 'comentario', 'nota')
    
class FilmesCriar(CreateView):
    model = Filme
    form_class = FilmeForm
    template_name = 'adicionar_filme.html'
    
class FilmesEditar(UpdateView):
    model = Filme
    form_class = EditFilmeForm
    template_name = 'filme_editar.html'
    
class AtoresCriar(CreateView):
    model = Ator
    form_class = AtorForm
    template_name = 'adicionar_ator.html'
    
class AtoresEditar(UpdateView):
    model = Ator
    form_class = EditAtorForm
    template_name = 'ator_editar.html'
    
class DiretoresCriar(CreateView):
    model = Diretor
    form_class = DiretorForm
    template_name = 'adicionar_diretor.html'
    
class DiretoresEditar(UpdateView):
    model = Diretor
    form_class = EditDiretorForm
    template_name = 'diretor_editar.html'

class FavoritosCriar(CreateView):
    model = Favoritos
    form_class = FavoritoForm
    template_name = 'adicionar_favorito.html'
    
class FavoritosEditar(UpdateView):
    model = Favoritos
    template_name = 'favoritos_editar.html'
    form_class = EditFavoritoForm
    
class AvaliacoesExcluir(DeleteView):
    model = Avaliacao
    template_name = 'avaliacoes_excluir.html'
    success_url = reverse_lazy('home')
    
class FilmesExcluir(DeleteView):
    model = Filme
    template_name = 'filmes_excluir.html'
    success_url = reverse_lazy('home')
    
class DiretoresExcluir(DeleteView):
    model = Diretor
    template_name = 'diretores_excluir.html'
    success_url = reverse_lazy('home')
    
class AtoresExcluir(DeleteView):
    model = Ator
    template_name = 'atores_excluir.html'
    success_url = reverse_lazy('home')
    