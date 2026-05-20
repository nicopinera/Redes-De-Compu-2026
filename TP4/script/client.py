import socket, json
from datetime import datetime
from cryptography.fernet import Fernet

def cargar_clave():
    with open("secret.key",'rb') as key:
        return key.read()

def main():
    KEY = cargar_clave()
    cifrado = Fernet(KEY)
    print("Inicializando Cliente")
    ip = input("Ingrese una IP:")
    puerto = int(input("Ingrese un puerto:"))
    # Se crea el socket de la familia internet, con protocolo TCP
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Conexion de cliente con servidor
    client.connect((ip, puerto))

    while True:
        try:
            msj=input("CLIENTE>")
            msj_bytes = msj.encode("utf-8")
            msj_cifrado = cifrado.encrypt(msj_bytes).decode("utf-8")
            ahora = datetime.now()
            message = {
                "nombre_grupo": "Puerto 1337",
                "payload": msj_cifrado,
                "timestamp": ahora.isoformat()
            }
            client.sendall(json.dumps(message).encode("utf-8"))
        except KeyboardInterrupt as e:
            print("Saliendo del cliente")
            client.close() # Cierre de conexion
            break

if __name__=="__main__":
    main()