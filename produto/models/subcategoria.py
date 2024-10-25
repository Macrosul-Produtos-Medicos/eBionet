from django.db import models
from django.utils.text import slugify

from core.models import BaseModel

class Subcategoria(BaseModel):
    
    nome = models.CharField('Subcategoria', unique=True, blank=False, null=False, max_length=64)
    slug = models.SlugField('Slug da subcategoria', blank=True, null=True, max_length=64)
    
    def __str__(self) -> str:
        return f"{self.nome}"
    
    class Meta:
        verbose_name = 'Subcategoria'
        verbose_name_plural = 'Subcategorias'
        
    def save(self, *args, **kwargs):
        self.slug = slugify(self.nome)
        super(Subcategoria, self).save(*args, **kwargs)
        
    def get_modelos(self):
        return self.modelos.all()
        
    