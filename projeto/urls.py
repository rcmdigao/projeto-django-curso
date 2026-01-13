"""
URL configuration for projeto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin #importa o modulo admin para configurar o admin do django
from django.urls import include, path #importa o modulo include para incluir as urls de outras apps e o modulo path para definir as urls da app
from django.conf.urls.static import static #importa o modulo static para adicionar as urls de media para o servidor de desenvolvimento
from django.conf import settings #importa o modulo settings para configurar as urls de media

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('recipes.urls')), # / + Nome APP.urls
]

# Adiciona as urls de media para o servidor de desenvolvimento
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Adiciona as urls de static para o servidor de desenvolvimento
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)