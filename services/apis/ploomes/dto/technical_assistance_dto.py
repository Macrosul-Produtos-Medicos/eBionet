import re
from dataclasses import dataclass, field


@dataclass
class TechnicalAssistanceDto:
    id: int
    nome_assistencia: str
    slug_assistencia: str
    nome_legal_assistencia: str
    logradouro_assistencia: str
    complemento_logradouro_assistencia: str
    bairro_assistencia: str
    cidade_assistencia: str
    estado_abrev_assistencia: str
    estado_assistencia: str
    cep_assistencia: str
    cep_default_assistencia: str = field(init=False)
    endereco_completo_assistencia: str = field(init=False)
    latitude_assistencia: str
    longitude_assistencia: str
    telefone_assistencia: str
    email_assistencia: str
    site_assistencia: str
    crea_ativo_assistencia: bool
    assistencia_tecnica_autorizada: bool
    subcategorias_assistidas: list

    def __post_init__(self):
        cep_assistencia_str = str(self.cep_assistencia)
        self.endereco_completo_assistencia = (
            f'{self.logradouro_assistencia} - {self.complemento_logradouro_assistencia} - {self.bairro_assistencia} - {self.cidade_assistencia} - {self.estado_assistencia} - {cep_assistencia_str[:5]}-{cep_assistencia_str[5:]}'
            if self.complemento_logradouro_assistencia != ''
            else f'{self.logradouro_assistencia} - {self.bairro_assistencia} - {self.cidade_assistencia} - {self.estado_assistencia} - {cep_assistencia_str[:5]}-{cep_assistencia_str[5:]}'
        )

        self.telefone_assistencia = self.__formatNumber(self.telefone_assistencia)
        self.cep_default_assistencia = self.__getCepDefaultForStates(self.estado_abrev_assistencia)

    def __getCepDefaultForStates(self, state: str):
        states = {
            'AC': '69900034',
            'AL': '57010001',
            'AP': '68900010',
            'AM': '69010060',
            'BA': '40020340',
            'CE': '60160150',
            'DF': '70040010',
            'ES': '29010003',
            'GO': '74013030',
            'MA': '65010010',
            'MT': '65908605',
            'MS': '79002002',
            'MG': '30130110',
            'PA': '66010020',
            'PB': '58011005',
            'PR': '80410210',
            'PE': '52050500',
            'PI': '64000010',
            'RJ': '20230010',
            'RN': '59010030',
            'RS': '90040194',
            'RO': '76801004',
            'RR': '69301160',
            'SC': '88010290',
            'SP': '01025020',
            'SE': '49010020',
            'TO': '77001004',
        }

        try:
            return states[state.upper()]
        except KeyError:
            return ''

    def __formatNumber(self, number):
        # Remover todos os caracteres não numéricos
        clean_number = re.sub(r'\D', '', number)

        # Checar o tamanho do número
        if len(clean_number) == 11:
            return re.sub(r'(\d{2})(\d{5})(\d{4})', r'(\1) \2-\3', clean_number)
        elif len(clean_number) == 10:
            return re.sub(r'(\d{2})(\d{4})(\d{4})', r'(\1) \2-\3', clean_number)
        else:
            return ''
