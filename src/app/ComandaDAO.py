from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src import db
from src.domain.entities.Comanda import Comanda
from src.infra.orm.ComandaModel import ComandaDB
from datetime import datetime

router = APIRouter(prefix="/comanda", tags=["Comanda"])

@router.post("/")
async def abrir_comanda(comanda: Comanda):
    session: Session = db.Session()
    try:
        nova = ComandaDB(**comanda.dict())
        session.add(nova)
        session.commit()
        return {"id": nova.id_comanda}
    except Exception as e:
        session.rollback()
        return {"erro": str(e)}
    finally:
        session.close()

@router.get("/")
async def listar_comandas():
    session = db.Session()
    try:
        return session.query(ComandaDB).all()
    finally:
        session.close()

@router.get("/{id}")
async def get_comanda(id: int):
    session = db.Session()
    try:
        return session.query(ComandaDB).filter(ComandaDB.id_comanda == id).first()
    finally:
        session.close()

@router.put("/{id}/fechar")
async def fechar_comanda(id: int):
    session = db.Session()
    try:
        comanda = session.query(ComandaDB).filter(ComandaDB.id_comanda == id).first()
        comanda.data_fechamento = datetime.utcnow()
        session.commit()
        return {"msg": "Comanda fechada"}
    except Exception as e:
        session.rollback()
        return {"erro": str(e)}
    finally:
        session.close()

@router.delete("/{id}")
async def deletar_comanda(id: int):
    session = db.Session()
    try:
        comanda = session.query(ComandaDB).filter(ComandaDB.id_comanda == id).first()
        session.delete(comanda)
        session.commit()
        return {"msg": "Comanda deletada"}
    except Exception as e:
        session.rollback()
        return {"erro": str(e)}
    finally:
        session.close()
