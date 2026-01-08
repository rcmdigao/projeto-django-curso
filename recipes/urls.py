from django.urls import path
from django.shortcuts import render
from recipes.views import home, sobre, contato # Colocar o caminho inteiro e as views.

urlpatterns = [
    path('', home), #/home/
    path('sobre/', sobre), #/quem/
    path('contato/', contato), #/contato/
]