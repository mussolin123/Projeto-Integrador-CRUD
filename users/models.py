from django.db import models

class User(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField(unique=True, null=False, blank=False)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"

    def __str__(self):
        return f"{self.nome} ({self.email})"

    
    
    