from django.urls import path
from django.shortcuts import render
from recipes.views import home # Colocar o caminho inteiro e as views.

urlpatterns = [
    path('', home), #/home/
]