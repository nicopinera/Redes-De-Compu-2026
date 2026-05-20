# Imagen base
FROM python:alpine

# Se crea la carpeta de trabajo a partir de ahora
WORKDIR /app

RUN pip install cryptography

COPY server.py secret.key /app/

# Puerto Expuesto
EXPOSE 5000

# Comando que se ejecuta automaticamente se levanta
CMD [ "python", "-u","server.py" ]