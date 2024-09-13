import socket

# Definir IP y puerto del servidor
HOST = '0.0.0.0'  # Escuchar en todas las interfaces
PORT = 8080      # Puerto donde se escuchará

# Crear el socket TCP/IP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)  # Escuchar solo una conexión

print(f"Servidor escuchando en {HOST}:{PORT}...")

# Aceptar la conexión del cliente
client_socket, client_address = server_socket.accept()
print(f"Conexión establecida con {client_address}")

while True:
    # Recibir el mensaje del cliente
    data = client_socket.recv(1024)
    if not data:
        break
    print(f"Cliente: {data.decode()}")

    # Enviar una respuesta al cliente
    response = input("Servidor: ")
    client_socket.sendall(response.encode())

# Cerrar la conexión
client_socket.close()
server_socket.close()
