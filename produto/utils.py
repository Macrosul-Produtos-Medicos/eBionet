from .models.dto.arquivo_conteudo_apoio_dto import ArquivoConteudoApoioDto
from .models.dto.conteudo_apoio_dto import ConteudoApoioDto
from .models.dto.modelo_dto import ModeloDto
from .models.dto.produto_dto import ProdutoDto
from .models.dto.video_produto_dto import VideoProdutoDto
from .models import ArquivoConteudoApoio, ConteudoApoio, Modelo, Produto, VideoProduto

from django.db.models import QuerySet



def get_support_content_file_dto(support_content_file : ArquivoConteudoApoio) -> ArquivoConteudoApoioDto:
    
    nome_arquivo = support_content_file.nome_arquivo if support_content_file.nome_arquivo else ''
    
    dto = ArquivoConteudoApoioDto(
        id=support_content_file.pk
        ,arquivo=support_content_file.arquivo.url
        ,nome_arquivo=nome_arquivo
        ,conteudo_apoio=support_content_file.conteudo_apoio.pk
    )
    
    return dto


def get_support_content_files_dto(support_content_files : QuerySet[ArquivoConteudoApoio]) -> list:

    support_content_list = []
    for support_content_file in support_content_files:
        support_content_file_dto = get_support_content_file_dto(support_content_file)
        support_content_list.append(support_content_file_dto.__dict__)
    
    return support_content_list

def get_support_content_dto(support_content : ConteudoApoio) -> ConteudoApoioDto:
    
    arquivos_conteudo_apoio = support_content.get_arquivos_conteudo_apoio()
    arquivos_conteudo_apoio = get_support_content_files_dto(arquivos_conteudo_apoio)
    
    dto = ConteudoApoioDto(
        id=support_content.pk
        ,nome=support_content.nome
        ,icone=support_content.icone
        ,modelo=support_content.modelo.pk
        ,arquivos_conteudo_apoio=arquivos_conteudo_apoio
    )
    
    return dto


def get_support_contents_dto(support_contents : QuerySet[ConteudoApoio]) -> list:
    
    support_content_list = []
    for support_content in support_contents:
        support_content_dto = get_support_content_dto(support_content)
        support_content_list.append(support_content_dto.__dict__)
    return support_content_list


def get_product_video_dto(product_video : VideoProduto) -> VideoProdutoDto:
    label = product_video.label if product_video.label else ''
    dto = VideoProdutoDto(
        id=product_video.pk
        ,video_url=product_video.video_url
        ,label=label
        ,produto=product_video.produto.pk
    )
    
    return dto


def get_product_videos_dto(product_videos : QuerySet[VideoProduto]) -> list:
    
    product_video_list = []
    for product_video in product_videos:
        product_video_dto = get_product_video_dto(product_video)
        product_video_list.append(product_video_dto.__dict__)
    return product_video_list
    

def get_product_dto(product : Produto) -> ProdutoDto:
    
    videos_produto = product.get_videos_produto()
    videos_produto = get_product_videos_dto(videos_produto)
    
    dto = ProdutoDto(
        id=product.pk
        ,nome=product.nome
        ,slug=product.slug
        ,modelo=product.modelo.pk
        ,videos_produto=videos_produto
    )
    
    return dto

def get_products_dto(products : QuerySet[Produto]) -> list:
    
    product_list = []
    for product in products:
        product_dto = get_product_dto(product)
        product_list.append(product_dto.__dict__)
    return product_list


def get_model_dto(model : Modelo) -> ModeloDto:
    
    conteudos_apoio = model.get_conteudos_apoio_by_name('software')
    conteudos_apoio = get_support_contents_dto(conteudos_apoio)
    
    conteudos_apoio_pacs = model.get_conteudos_apoio_by_name('pacs')
    conteudos_apoio += get_support_contents_dto(conteudos_apoio_pacs)
    
    
    
    produtos = model.get_produtos()
    produtos = get_products_dto(produtos)
    
    dto = ModeloDto(
        id=model.pk
        ,nome=model.nome
        ,slug=model.slug
        ,subcategoria=model.subcategoria.pk
        ,conteudos_apoio=conteudos_apoio
        ,produtos=produtos
    )
    
    return dto


def get_models_by_subcategory_dto(subcategory_id : int) -> list:
    
    models = Modelo.objects.filter(subcategoria__pk=subcategory_id)
    model_list = []
    for model in models:
        model_dto = get_model_dto(model)
        model_list.append(model_dto.__dict__)
    
    return model_list


def get_support_contents_by_name_dto(support_content_name : str) -> list:
    
    support_contents = ConteudoApoio.objects.filter(nome__icontains=support_content_name)
    support_content_list = []
    for support_content in support_contents:
        support_content_dto = get_support_content_dto(support_content)
        support_content_list.append(support_content_dto.__dict__)
    return support_content_list