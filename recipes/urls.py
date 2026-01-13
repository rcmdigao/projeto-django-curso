# Quando o arquivo esta em outra pasta, colocar o nome da pasta e o nome do arquivo.
from django.urls import path
# from . import views > Quando os arquivos estao na mesma pasta (Irmao)
from . import views

#recipes:recipe é o nome da url
app_name = 'recipes'

urlpatterns = [
    path('', views.home, name='home'), #/home/
    path('recipes/<slug:id>/', views.recipe, name='recipe'), #/recipes/1/
]   #slug:id é um parametro que sera passado na url e sera usado na view para buscar a receita