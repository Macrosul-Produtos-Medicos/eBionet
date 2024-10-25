from django.db import models

from core.models import BaseModel

from .modelo import Modelo


class ConteudoApoio(BaseModel):
    nome = models.CharField(max_length=64, blank=False, null=False)
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE, related_name='conteudos_apoio', null=True, blank=True)
    para_vet = models.BooleanField(default=False)

    class Meta:
        ordering = ('id',)
        verbose_name = 'Conteúdo de apoio'
        verbose_name_plural = 'Conteúdos de apoio'

    def __str__(self):
        return f'{self.nome}'

    def get_arquivos_conteudo_apoio(self):
        return self.arquivos_conteudo_apoio.all()