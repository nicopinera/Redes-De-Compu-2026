import socket, json, time
from datetime import datetime

# Definicion de IP y Puerto del servidor donde nos queremos conectar
HOST = "127.0.0.1"
PORT = 5000

# Fecha y hora actual
ahora = datetime.now()

# Mensaje a enviar
message = {
    "nombre_grupo": "Puerto 1337",
    "payload": "Hola servidor",
    "timestamp": ahora.isoformat()
}

# Se crea el socket de la familia internet, con protocolo TCP
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conexion de cliente con servidor
client.connect((HOST, PORT))

# Se convierte el diccionario a json
client.sendall(json.dumps(message).encode("utf-8"))

# Cierre de conexion
client.close()