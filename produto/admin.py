from django.contrib import admin

from .models import (
    ArquivoConteudoApoio,
    ConteudoApoio,
    ImagemProduto,
    Modelo,
    Produto,
    Subcategoria,
    VideoProduto,
)

class ArquivoConteudoApoioInLine(admin.TabularInline):
    model = ArquivoConteudoApoio
    extra = 0
    readonly_fields = ('criado_em', 'modificado_em')


@admin.register(ConteudoApoio)
class ConteudoApoioAdmin(admin.ModelAdmin):
    inlines = (ArquivoConteudoApoioInLine,)
    list_display = ('__str__', 'nome', 'modelo')
    readonly_fields = ('criado_em', 'modificado_em')


@admin.register(Modelo)
class ModeloAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'nome', 'subcategoria', 'imagem_principal')
    readonly_fields = ('criado_em', 'modificado_em')
    list_editable = ('nome', 'imagem_principal', 'subcategoria')
    
class ImagemProdutoInline(admin.TabularInline):
    model = ImagemProduto
    extra = 0
    readonly_fields = ('criado_em', 'modificado_em')
    
    
class VideoProdutoInline(admin.TabularInline):
    model = VideoProduto
    extra = 0
    readonly_fields = ('criado_em', 'modificado_em')


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    inlines = (ImagemProdutoInline, VideoProdutoInline)
    list_display = (
        'slug',
        'nome',
        'cod_sap_item',
        'modelo',
        'ean',
    )
    readonly_fields = ('criado_em', 'modificado_em')
    list_filter = ('modelo',)
    search_fields = ('nome',)
    list_editable = (
        'nome',
        'cod_sap_item',
        'modelo',
        'ean',
    )
           
@admin.register(Subcategoria)
class SubcategoriaAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'nome', 'slug')
    readonly_fields = ('criado_em', 'modificado_em', 'slug')
    list_editable = (
        'nome',
    )

