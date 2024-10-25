from dataclasses import dataclass, field

@dataclass
class ProdutoDto:
    id : int
    nome : str
    slug : str
    cod_sap_item : str = field(init=False)
    modelo : int
    ean : int = field(init=False)
    videos_produto : list