from pydantic import BaseModel

class Produto(BaseModel):
    nome: str
    preco: int
    foto: bytes = None  # Campo BLOB (opcional)
