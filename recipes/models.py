from django.contrib.auth.models import User
from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=65)
    descricao = models.CharField(max_length=165)
    slug = models.SlugField()
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    
    def __str__(self): #retorna o nome da coluna nome
        return self.nome

# Create your models here.
class Recipe(models.Model):
    titulo = models.CharField(max_length=65)
    descricao = models.CharField(max_length=165)
    slug = models.SlugField()
    tempo_preparo = models.IntegerField()
    tempo_preparo_unidade = models.CharField(max_length=65)
    rendimento = models.IntegerField()
    rendimento_unidade = models.CharField(max_length=65)
    passos_preparo = models.TextField()
    passos_preparo_is_html = models.BooleanField(default=False) #se o campo passos_preparo é html?
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)     
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)
    autor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    cover = models.ImageField(upload_to='recipes/covers/%Y/%m/%d/', blank=True, default='')

    def __str__(self): #retorna o nome da coluna titulo
        return self.titulo