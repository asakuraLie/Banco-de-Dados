from django.contrib import admin

from .models import *

admin.site.register(Usuario)
admin.site.register(Filme)
admin.site.register(Avaliacao)
admin.site.register(Favoritos)
admin.site.register(Ator)
admin.site.register(Diretor)

# Register your models here.
