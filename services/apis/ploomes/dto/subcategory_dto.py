from dataclasses import dataclass


@dataclass
class SubcategoryDto:
    id: int
    nome_subcategoria: str
    slug_subcategoria: str
    field_id_other_properties: int
