# Imagen base
FROM python:alpine

# Se crea la carpeta de trabajo a partir de ahora
WORKDIR /app

COPY server.py .

# Puerto Expuesto
EXPOSE 5000

# Comando que se ejecuta automaticamente se levanta
CMD [ "python", "-u","server.py" ]