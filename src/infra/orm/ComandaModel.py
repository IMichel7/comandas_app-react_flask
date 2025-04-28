from sqlalchemy import Column, Integer, DateTime, ForeignKey
from src.db import Base
from datetime import datetime

class ComandaDB(Base):
    __tablename__ = "tb_comanda"

    id_comanda = Column(Integer, primary_key=True, autoincrement=True)
    id_funcionario = Column(Integer, ForeignKey("tb_funcionario.id_funcionario"))
    id_cliente = Column(Integer, ForeignKey("tb_cliente.id_cliente"))
    data_abertura = Column(DateTime, default=datetime.utcnow)
    data_fechamento = Column(DateTime, nullable=True)
