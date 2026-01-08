from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(
        request, 'recipes/home.html', 
        context={'name':'Rodrigo Cunha Machado'}
        )

def sobre(request):
    return HttpResponse('Quem Somos')

def contato(request):
    return HttpResponse('Fale Conosco')