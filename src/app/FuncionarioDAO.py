from src import db  # <-- corrigido aqui!
from src.infra.orm.FuncionarioModel import FuncionarioDB
from src.domain.entities.Funcionario import Funcionario
from fastapi import APIRouter, Depends
from src.security import verify_token

router = APIRouter(dependencies=[Depends(verify_token)])

# o resto do seu código abaixo permanece igual


@router.get("/funcionario/", tags=["Funcionário"])
async def get_funcionarios():
    try:
        session = db.Session()
        dados = session.query(FuncionarioDB).all()
        return dados, 200
    except Exception as e:
        return {"erro": str(e)}, 400
    finally:
        session.close()

# Exemplo de POST
@router.post("/funcionario/", tags=["Funcionário"])
async def post_funcionario(corpo: Funcionario):
    try:
        session = db.Session()
        dados = FuncionarioDB(None, corpo.nome, corpo.matricula,
                              corpo.cpf, corpo.telefone, corpo.grupo, corpo.senha)
        session.add(dados)
        session.commit()
        return {"id": dados.id_funcionario}, 200
    except Exception as e:
        session.rollback()
        return {"erro": str(e)}, 400
    finally:
        session.close()
