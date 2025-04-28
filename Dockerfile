# Utiliza a imagem base Python 3.13-alpine
FROM python:3.13-alpine

# Metadados da imagem (opcional, mas recomendado)
LABEL maintainer="Seu Nome <seu.email@exemplo.com>"
LABEL description="API Python com FastAPI, Hypercorn e suporte a QUIC/HTTP2/HTTP3"
LABEL version="1.0.0"

# Define o diretório de trabalho
WORKDIR /code

# Instala as dependências de compilação necessárias
RUN apk add --no-cache gcc musl-dev libffi-dev openssl-dev python3-dev

# --- Instalação de Dependências ---
# Copia primeiro o requirements.txt para aproveitar o cache do Docker
COPY ./requirements.txt .

# Atualiza o pip e instala as dependências
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copia o código-fonte da aplicação
COPY ./src /code

# --- Execução ---
# Expõe a porta 4443 para TCP (HTTPS) e UDP (para QUIC/H3)
EXPOSE 4443/tcp
EXPOSE 4443/udp

# Comando para iniciar o servidor Hypercorn (não utilizar --reload em produção)
CMD ["hypercorn", "--certfile=/cert/cert.pem", "--keyfile=/cert/ecc-key.pem", "--bind", "0.0.0.0:4443", "--quic-bind", "0.0.0.0:4443", "main:app"]
