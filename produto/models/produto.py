from django.db import models
from django.utils.text import slugify

from .modelo import Modelo

from core.models import BaseModel

class Produto(BaseModel):
    
    nome = models.CharField('Produto', unique=True, blank=False, null=False, max_length=64)
    slug = models.SlugField('Slug do produto', blank=True, null=True, max_length=64)
    cod_sap_item = models.CharField('Código SAP do Produto', blank=True, null=True, max_length=8)
    modelo = models.ForeignKey(
        Modelo,
        on_delete=models.CASCADE,
        related_name='produtos',
    )
    ean = models.CharField(max_length=16, null=True, blank=True)
    
    def __str__(self) -> str:
        return f"{self.nome}"
    
    class Meta:
        verbose_name = 'Modelo'
        verbose_name_plural = 'Modelos'
        
    def save(self, *args, **kwargs):
        self.slug = slugify(self.nome)
        super(Produto, self).save(*args, **kwargs)
        
    
    def get_imagens_produto(self):
        return self.imagens_produto.all()
    
    def get_videos_produto(self):
        return self.videos_produto.all()