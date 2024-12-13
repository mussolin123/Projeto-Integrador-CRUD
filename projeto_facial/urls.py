from django.contrib import admin  # Adiciona esta importação
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from alunos.views import home  # Importe a view home do app alunos

urlpatterns = [
    path('', home, name='home'),  # Definindo a URL raiz para a view home
    path('admin/', admin.site.urls),  # Rota para o painel de administração
    path('api/', include('alunos.urls')),  # Inclui as rotas do app alunos
]

# Configuração para servir arquivos de mídia no desenvolvimento
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)