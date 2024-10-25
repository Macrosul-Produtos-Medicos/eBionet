from django.db import models
from django.utils.text import slugify

from tinymce.models import HTMLField

from .subcategoria import Subcategoria
from core.models import BaseModel

class Modelo(BaseModel):
    
    nome = models.CharField('Modelo', unique=True, blank=False, null=False, max_length=64)
    apresentacao = models.CharField('Apresentação do modelo', blank=True, null=True, max_length=512)
    especificacoes = HTMLField('Especificações do produto', blank=True, null=True)
    slug = models.SlugField('Slug do modelo', blank=True, null=True, max_length=64)
    imagem_principal = models.URLField('Imagem principal do modelo', blank=False, null=False, max_length=256)
    subcategoria = models.ForeignKey(
        Subcategoria,
        on_delete=models.CASCADE,
        related_name='modelos',
    )
    
    
    def __str__(self) -> str:
        return f"{self.nome}"
    
    class Meta:
        verbose_name = 'Modelo'
        verbose_name_plural = 'Modelos'
        
    def save(self, *args, **kwargs):
        self.slug = slugify(self.nome)
        super(Modelo, self).save(*args, **kwargs)
        
    
    def get_conteudos_apoio(self):
        return self.conteudos_apoio.all()

    def get_produtos(self):
        return self.produtos.all()