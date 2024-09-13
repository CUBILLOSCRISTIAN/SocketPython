import socket

# Definir IP y puerto del servidor al que se conectará
SERVER_HOST = '192.168.1.15'  # IP del servido
SERVER_PORT = 8080             # Puerto del servidor

# Crear el socket TCP/IP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Intentar conectarse al servidor
client_socket.connect((SERVER_HOST, SERVER_PORT))
print(f"Conectado al servidor {SERVER_HOST}:{SERVER_PORT}")

while True:
    # Enviar un mensaje al servidor
    message = input("Cliente: ")
    client_socket.sendall(message.encode())

    # Recibir la respuesta del servidor
    data = client_socket.recv(1024)
    if not data:
        break
    print(f"Servidor: {data.decode()}")

# Cerrar la conexión
client_socket.close()
