
from django.db import models

from core.models import BaseModel
from .produto import Produto


class VideoProduto(BaseModel):
    video_url = models.URLField(max_length=256, null=True, blank=True)
    label = models.CharField(max_length=128, null=True, blank=True)
    produto = models.ForeignKey(
        Produto,
        on_delete=models.CASCADE,
        related_name='videos_produto',
    )

    class Meta:
        ordering = ('pk',)
        verbose_name = 'Video do Produto'
        verbose_name_plural = 'Videos do Produto'

    def __str__(self):
        return f'{self.pk}'