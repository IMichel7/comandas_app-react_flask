from dotenv import load_dotenv, find_dotenv
import os

# Carrega variáveis do arquivo .env
dotenv_file = find_dotenv()
load_dotenv(dotenv_file)

# Configurações da API
HOST = os.getenv("HOST", "127.0.0.1")
PORT = int(os.getenv("PORT", 8000))
RELOAD = os.getenv("RELOAD", "True").lower() in ["true", "1", "yes"]

# Configurações do banco de dados
DB_SGDB = os.getenv("DB_SGDB", "sqlite")
DB_NAME = os.getenv("DB_NAME", "apiDatabase")
DB_HOST = os.getenv("DB_HOST", "127.0.0.1")
DB_USER = os.getenv("DB_USER", "root")
DB_PASS = os.getenv("DB_PASS", "")

# Monta a string de conexão com base no SGBD escolhido
if DB_SGDB == "sqlite":
    STR_DATABASE = f"sqlite:///{DB_NAME}.db"
elif DB_SGDB == "mysql":
    import pymysql
    STR_DATABASE = f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}?charset=utf8mb4"
elif DB_SGDB == "mssql":
    import pymssql
    STR_DATABASE = f"mssql+pymssql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}?charset=utf8"
else:
    STR_DATABASE = f"sqlite:///apiDatabase.db"  # fallback

# Segurança JWT
SECRET_KEY = os.getenv("SECRET_KEY", "chave-secreta-padrao")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))
