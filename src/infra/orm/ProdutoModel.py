from src import db
from sqlalchemy import Column, VARCHAR, Integer, LargeBinary

class ProdutoDB(db.Base):
    __tablename__ = 'tb_produto'

    id_produto = Column(Integer, primary_key=True, autoincrement=True, index=True)
    nome = Column(VARCHAR(100), nullable=False, index=True)
    preco = Column(Integer, nullable=False)
    foto = Column(LargeBinary, nullable=True)  # Campo BLOB

    def __init__(self, id_produto, nome, preco, foto):
        self.id_produto = id_produto
        self.nome = nome
        self.preco = preco
        self.foto = foto
