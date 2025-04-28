from pydantic import BaseModel

class Funcionario(BaseModel):
    nome: str
    matricula: str
    cpf: str
    telefone: str
    grupo: int
    senha: str
