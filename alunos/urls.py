from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AlunoViewSet, reconhecer_aluno

# Roteador para a API de alunos
router = DefaultRouter()
router.register(r'alunos', AlunoViewSet)  # Essa é a rota do CRUD de alunos

urlpatterns = [
    path('', include(router.urls)),  # O prefixo 'alunos' será adicionado na URL
    path('reconhecer/', reconhecer_aluno, name='reconhecer_aluno'),  # Endpoint para reconhecimento
    
]