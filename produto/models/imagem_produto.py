from urllib.parse import unquote

from django.db import models

from core.models import BaseModel
from .produto import Produto


class ImagemProduto(BaseModel):
    foto = models.FileField(upload_to='', max_length=300, null=True, blank=True)
    produto = models.ForeignKey(
        Produto,
        on_delete=models.CASCADE,
        related_name='imagens_produto',
    )

    class Meta:
        ordering = ('pk',)
        verbose_name = 'Produto foto'
        verbose_name_plural = 'Produto fotos'

    def __str__(self):
        return f'{self.pk}'