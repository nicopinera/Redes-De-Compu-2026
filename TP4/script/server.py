import socket
import threading
import json
from datetime import datetime

HOST = "0.0.0.0"
PORT = 5000
BUFFER_SIZE = 1024


def handle_client(client_socket, client_address):
    ip_address = client_address[0]

    print(f"Hola {ip_address},bienvenido al servidor!")

    try:
        while True:
            data = client_socket.recv(BUFFER_SIZE)

            # Si el cliente envia vacio se rompe el bucle
            if not data:
                break

            try:
                # Se convierte el mensaje en un diccionario de python
                message = json.loads(data.decode("utf-8"))

                if (
                    isinstance(message, dict) # Se verifica que sea un diccionario
                    and "nombre_grupo" in message
                    and "payload" in message
                    and isinstance(message["nombre_grupo"], str)
                    and isinstance(message["payload"], str)
                ):
                    print("---"*10)
                    print(f"Grupo: {message['nombre_grupo']}\nMensaje: {message['payload']}\nInstante {datetime.now()}")
                    print("---"*10)
                else:
                    print(f"{ip_address}: Esperando mensaje en formato correcto")

            except json.JSONDecodeError:
                print(f"{ip_address}: Esperando mensaje en formato correcto")

    except ConnectionResetError:
        pass

    finally:
        print(f"Bye {ip_address}!")
        client_socket.close()


def main():
    # Creo el socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Asigno el socket con la direccion IP y el puerto
    server_socket.bind((HOST, PORT))

    # Empiezo a escuchar conexiones entrante
    server_socket.listen()

    print(f"Servidor escuchando en {HOST}:{PORT}")

    try:
        while True:
            # Se optiene el socket por donde van a comunicarse con el cliente y la informacion del cliente
            client_socket, client_address = server_socket.accept()

            # Se crea un hilo y se le asigna la funcion del handle_cliente con el socket y la informacion del cliente
            client_thread = threading.Thread(
                target=handle_client,
                args=(client_socket, client_address)
            )

            # Se inicia el hilo
            client_thread.start()

    except KeyboardInterrupt:
        print("\nSe detiene el servidor")

    finally:
        # Se cierra el socket
        server_socket.close()


if __name__ == "__main__":
    main()