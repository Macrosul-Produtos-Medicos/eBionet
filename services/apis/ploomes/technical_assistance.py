from itertools import groupby

from django.utils.text import slugify


from services.apis.ploomes.dto.subcategory_dto import SubcategoryDto
from services.apis.ploomes.dto.technical_assistance_dto import TechnicalAssistanceDto
from services.apis.ploomes.ploomes_api import PloomesApi



class TechnicalAssistance:
    EARTH_DIAMETER = 12742
    PRODUTOS_ASSISTIDOS = 327120
    STATUS_CLIENTE = 122136
    EX_CLIENTE = 6538633
    ASSISTENCIA_TECNICA_AUTORIZADA = 277440
    RECEM_INATIVADO = 16289051

    def __init__(self):
        self.ploomes_api = PloomesApi('https://api2.ploomes.com/')

    

    def __getTechnicalAssistenceDto(self, assistencia: dict) -> TechnicalAssistanceDto:
        """Retorna um dto de uma assistencia técnica, vinda do acesso a API do ploomes.

        Args:
            assistencia (dict): Assistência técnica.

        Returns:
            TechnicalAssistanceDto: Dto da assistência técnica.
        """

        def return_empty_string_if_null(x):
            return '' if x is None else x

        tem_crea_ativo = False

        # Verifica se o campo
        try:
            telefone = str(assistencia['Phones'][0]['SearchPhoneNumber'])
        except:  # noqa E722
            telefone = ''

        try:
            crea = assistencia['Tags'][0]['TagId']
            tem_crea_ativo = True if crea == 140426 else False
        except:  # noqa E722
            tem_crea_ativo = False

        dto = TechnicalAssistanceDto(
            id=assistencia['Id'],
            nome_assistencia=assistencia['Name'],
            slug_assistencia=slugify(assistencia['Name']),
            nome_legal_assistencia=assistencia['LegalName'],
            logradouro_assistencia=assistencia['StreetAddress'],
            complemento_logradouro_assistencia=return_empty_string_if_null(assistencia['StreetAddressLine2']),
            bairro_assistencia=assistencia['Neighborhood'],
            cidade_assistencia=assistencia['City']['Name'],
            estado_abrev_assistencia=assistencia['State']['Short'],
            estado_assistencia=assistencia['State']['Name'],
            cep_assistencia=assistencia['ZipCode'],
            latitude_assistencia=assistencia['Latitude'],
            longitude_assistencia=assistencia['Longitude'],
            telefone_assistencia=telefone,
            email_assistencia=assistencia['Email'],
            site_assistencia=assistencia['Website'],
            crea_ativo_assistencia=tem_crea_ativo,
            assistencia_tecnica_autorizada=True,
            subcategorias_assistidas=[],
        )

        return dto

    def __getAllAssistancesFromRequest(self, request_values: list) -> list[TechnicalAssistanceDto]:
        """Pega todas as categoria de um request, resultado do acesso à API da ploomes.

        Args:
            request (list): Resultado do acesso à API da ploomes.

        Returns:
            list[TechnicalAssistanceDto]: Lista de dto de assistências técnicas
        """

        assistencias_tecnicas = []
        assistances = request_values

        # para cada assistencia
        for assistance in assistances:
            eh_ex_cliente = False
            eh_assistencia_tecnica_autorizada = True
            subcategorias = []

            # dto da assistencia
            assistencia_dto = self.__getTechnicalAssistenceDto(assistance)

            # para cada outra propriedade
            for other_properties in assistance['OtherProperties']:
                # se for o campo que representa a subcategoria que aquele assistencia atende
                if other_properties['FieldId'] == TechnicalAssistance.PRODUTOS_ASSISTIDOS:
                    subcategorias.append(f"{slugify(other_properties['ObjectValueName'])}")

                if (
                    other_properties['ObjectValueId'] == TechnicalAssistance.EX_CLIENTE
                    or other_properties['ObjectValueId'] == TechnicalAssistance.RECEM_INATIVADO
                ):  # noqa E501
                    eh_ex_cliente = True

                # se for o campo que representa se a assistencia é uma autorizada
                if other_properties['FieldId'] == TechnicalAssistance.ASSISTENCIA_TECNICA_AUTORIZADA:
                    # se não for, define que não é
                    if not other_properties['BoolValue']:
                        eh_assistencia_tecnica_autorizada = False
                        assistencia_dto.assistencia_tecnica_autorizada = eh_assistencia_tecnica_autorizada

            assistencia_dto.subcategorias_assistidas = subcategorias
            if eh_assistencia_tecnica_autorizada and not eh_ex_cliente:
                assistencias_tecnicas.append(assistencia_dto.__dict__)

        return assistencias_tecnicas

    def __getAssistanceBySubcategory(
        self, technical_assistances: list, subcategory: str
    ) -> list[TechnicalAssistanceDto]:  # noqa E501
        """Pega as assistencias por uma subcategoria específica.

        Args:
            technical_assistances (list): Lista com todas as assistências técnicas.
            subcategory (str): Uma subcategoria que pode (ou não) ser assistida.

        Returns:
            list[TechnicalAssistanceDto]: Uma lista com assistência que assiste essa subcategoria.
        """

        filter_list = []
        for assistance in technical_assistances:
            for subcategoria in assistance['subcategorias_assistidas']:
                if subcategory == subcategoria:
                    filter_list.append(assistance)
        return filter_list


    def getAssistances(self) -> dict:
        request_assistencias = self.ploomes_api.getAllDatas(
            'Contacts',
            filter='(((OtherProperties/any(o:+o/FieldId+eq+277440))))',
            expand='Phones($select=SearchPhoneNumber),City($select=Name),State($select=Name,Short),Tags($select=TagId),OtherProperties($select=FieldId, ObjectValueName, ObjectValueId, BoolValue)',  # noqa E501
            select='Id,Name,LegalName,StreetAddress,StreetAddressLine2,Neighborhood,ZipCode,Email,Website,Latitude,Longitude',  # noqa E501
        )
        assistencias_tecnicas = self.__getAllAssistancesFromRequest(request_assistencias['value'])

        return assistencias_tecnicas

    def getAllSubcategoriesHandledByTechnicalAssistance(self) -> list[SubcategoryDto]:
        """Acessa a api da ploomes e pega todas as subcategorias tradas pelas assistências técnicas.

        Para saber como funciona a api da ploomes acesse: https://developers.ploomes.com

        Returns:
            list[SubcategoryDto]: uma lista com os dtos da subcategoria.
        """

        request = self.__getAllDatas('Contacts')
        subcategorias = self.__getAllSubcategoriesFromRequest(request)

        return subcategorias
    
    
    def __joinAssistancesWithoutDuplicates(self, lista1 : list, lista2 : list):
        
        # Conjunto para armazenar nomes únicos
        nomes_unicos = set()
        # Lista final sem duplicatas
        lista_unica = []

        # Adiciona os elementos de lista1 e lista2
        for dicionario in lista1 + lista2:
            if dicionario['nome_assistencia'] not in nomes_unicos:
                nomes_unicos.add(dicionario['nome_assistencia'])
                lista_unica.append(dicionario)
                
        return lista_unica
    
    
    def getAllAssistances(self) -> list:
        
        subcategorias = ['Eletrocardiógrafos', 'Monitor de Sinais Vitais', 'Monitor Fetal & Cardiotocógrafo']
        assistencias = self.getAssistances()
        assistencias_sem_repeticao = []
        for subcategoria in subcategorias:
            assistencias = self.__getAssistanceBySubcategory(assistencias, slugify(subcategoria))
            assistencias_sem_repeticao = self.__joinAssistancesWithoutDuplicates(assistencias_sem_repeticao, assistencias)
        
        assistencias_sem_repeticao.sort(key=lambda x: x['estado_abrev_assistencia'])
        grupos = [
            {'estado': chave, 'itens': list(grupo)}
            for chave, grupo in groupby(assistencias_sem_repeticao, key=lambda x: x['estado_abrev_assistencia'])
        ]
        
        return grupos   
