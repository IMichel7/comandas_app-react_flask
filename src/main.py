from fastapi import FastAPI, Depends
from contextlib import asynccontextmanager
#Michel Furtado da Silva

from src import db
from src.settings import HOST, PORT, RELOAD
from src.app import FuncionarioDAO, ClienteDAO, ProdutoDAO, ComandaDAO
from src import security
from src.security import verify_token

# Ciclo de vida (cria tabelas ao iniciar)
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("API has started")
    await db.criaTabelas()
    yield
    print("API is shutting down")

# Cria a aplicação FastAPI com ciclo de vida
app = FastAPI(lifespan=lifespan)

# Rota padrão
@app.get("/", tags=["Rota padrão"])
async def root():
    return {
        "detail": "API Comandas",
        "Swagger UI": "http://127.0.0.1:8000/docs",
        "ReDoc": "http://127.0.0.1:8000/redoc"
    }

# Inclui rotas protegidas com JWT
app.include_router(security.router)  # <-- rota /token e /token/logado
app.include_router(FuncionarioDAO.router, dependencies=[Depends(verify_token)])
app.include_router(ClienteDAO.router, dependencies=[Depends(verify_token)])
app.include_router(ProdutoDAO.router, dependencies=[Depends(verify_token)])
app.include_router(ComandaDAO.router, dependencies=[Depends(verify_token)])

# Execução direta (opcional)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("src.main:app", host=HOST, port=int(PORT), reload=RELOAD)
