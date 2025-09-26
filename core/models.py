from django.db import models
from django.conf import settings

class Anotacao(models.Model):

    dono = models.ForeignKey(settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, related_name='anotacoes' )

    titulo = models.CharField(max_length=150)
    descricao = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo