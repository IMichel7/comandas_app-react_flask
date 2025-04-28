from pydantic import BaseModel
from datetime import datetime

class Comanda(BaseModel):
    id_funcionario: int
    id_cliente: int
    data_abertura: datetime
    data_fechamento: datetime | None = None
