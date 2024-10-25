from dataclasses import dataclass, field

@dataclass
class VideoProdutoDto:
    id : int
    video_url : str
    label : str
    produto : int
