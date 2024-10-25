from dataclasses import dataclass, field

@dataclass
class ModeloDto:
    id : int
    nome : str
    apresentacao : str = field(init=False)
    especificacoes : str = field(init=False)
    slug : str
    imagem_principal : str = field(init=False)
    subcategoria : int
    conteudos_apoio : list
    produtos : list