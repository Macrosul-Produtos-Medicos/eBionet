from django.db import models

from core.models import BaseModel

from .conteudo_apoio import ConteudoApoio


class ArquivoConteudoApoio(BaseModel):
    arquivo = models.FileField(upload_to='ConteudoApoio', max_length=256, null=False, blank=False)
    nome_arquivo = models.CharField(max_length=64, null=True, blank=True)
    conteudo_apoio = models.ForeignKey(ConteudoApoio, related_name='arquivos_conteudo_apoio', on_delete=models.CASCADE)

    class Meta:
        ordering = ('id',)
        verbose_name = 'Arquivo de conteúdo de apoio'
        verbose_name_plural = 'Arquivos de conteúdos de apoio'

    def __str__(self):
        return f'Arquivo - {self.pk}'