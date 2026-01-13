from django.contrib import admin

from .models import Categoria, Recipe

class CategoriaAdmin(admin.ModelAdmin):
    ...
class ReceitaAdmin(admin.ModelAdmin):
    ...
    
    
admin.site.register(Categoria, CategoriaAdmin) #registrando o modelo Categoria e a classe CategoriaAdmin
admin.site.register(Recipe, ReceitaAdmin) #registrando o modelo Recipe e a classe RecipeAdmin