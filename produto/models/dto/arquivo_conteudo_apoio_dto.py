from dataclasses import dataclass, field

@dataclass
class ArquivoConteudoApoioDto:
    id : int
    arquivo : str
    nome_arquivo : str
    conteudo_apoio : int