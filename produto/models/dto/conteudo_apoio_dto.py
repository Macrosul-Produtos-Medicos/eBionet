from dataclasses import dataclass, field

@dataclass
class ConteudoApoioDto:
    id : int
    nome : str
    icone : str
    modelo : int
    arquivos_conteudo_apoio : list