from django.urls import path, include
from .views import *

urlpatterns = [
    #path('', views.home, name="home")
    path('', HomeView.as_view(), name='home'),
    #path usuario
    path('usuario/<int:pk>', UsuarioDetail.as_view(), name='meu-usuario'),
    path('adc_usuario/', UsuarioCriar.as_view(), name='criar-usuario'),
    #path lista favoritos
    path('favoritos/', FavoritosView.as_view(), name='lista-favoritos'),
    path('favoritos/<int:pk>', FavoritosDetail.as_view(), name='minha-lista'),
    path('adc_favorito/', FavoritosCriar.as_view(), name='adc_favorito'),
    path('favoritos/editar/<int:pk>', FavoritosEditar.as_view(), name='editar-favoritos'),
    #path dos filmes
    path('filmes/', FilmeView.as_view(), name='filmes-disponiveis'),
    path('filmes_detail/<str:pk>', FilmeDetail.as_view(), name='filmes-detalhes'),
    path('filmes_detail/editar/<str:pk>', FilmesEditar.as_view(), name='filmes-editar'),
    path('filmes_detail/<str:pk>/excluir', FilmesExcluir.as_view(), name='filmes-excluir'),
    path('adc_filme/', FilmesCriar.as_view(), name='adc_filme'),
    #path dos atores
    path('atores/', AtoresView.as_view(), name='atores-listados'),
    path('atores-detail/<str:pk>', AtorDetail.as_view(), name='atores-detalhes'),
    path('atores-detail/editar/<str:pk>', AtoresEditar.as_view(), name='atores-editar'),
    path('atores-detail/<str:pk>/excluir', AtoresExcluir.as_view(), name='atores-excluir'),
    path('adc_atores/', AtoresCriar.as_view(), name='adc_ator'),
    #path dos diretores
    path('diretores/', DiretoresView.as_view(), name='diretores-listados'),
    path('diretores-detail/<str:pk>', DiretorDetail.as_view(), name='diretores-detalhes'),
    path('diretores-detail/editar/<str:pk>', DiretoresEditar.as_view(), name='diretores-editar'),
    path('diretores-detail/<str:pk>/excluir', DiretoresExcluir.as_view(), name='diretores-excluir'),
    path('adc_diretores/', DiretoresCriar.as_view(), name='adc_diretor'),
    #path das avaliações
    path('avaliacoes/', AvaliacoesView.as_view(), name="avaliacoes-lista"),
    path('avaliacoes/<int:pk>', AvalicoesDetail.as_view(), name="avaliacoes-detalhes"),
    path('avaliacoes/editar/<int:pk>', AvaliacoesEditar.as_view(), name="avaliacoes-editar"),
    path('avaliacoes/<int:pk>/excluir/', AvaliacoesExcluir.as_view(), name="avaliacoes-excluir"),
    path('adc_avaliacao/', AvaliacoesCriar.as_view(), name='adc_avaliacao'),
    path('avaliacao_por_filme/<str:fms>/', AvaliacoesPorFilme, name='avaliacao-por-filme'),
    path('avaliacao_por_usuario/<str:us>/', AvaliacoesPorUsuario, name='avaliacao-por-usuario'),
]
