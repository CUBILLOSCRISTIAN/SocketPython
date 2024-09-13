import socket
from Crypto.Cipher import Salsa20
import os

# Función para cifrar los datos
def encrypt_salsa20(key, plaintext, nonce):
    cipher = Salsa20.new(key=key, nonce=nonce)
    ciphertext = cipher.encrypt(plaintext)
    return ciphertext

# Función para descifrar los datos
def decrypt_salsa20(key, ciphertext, nonce):
    cipher = Salsa20.new(key=key, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext

# Crear el socket del servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_ip = '0.0.0.0'
server_port = 8080

server_socket.bind((server_ip, server_port))
server_socket.listen(5)
print(f"Esperando conexión del cliente... {server_ip}:{server_port}")

# Aceptar la conexión del cliente
client_socket, client_address = server_socket.accept()
print(f"Conexión aceptada de {client_address}")

# Generar una llave simétrica de 256 bits, 32 bytes
key = os.urandom(32)  
client_socket.sendall(key)

print("Llave simétrica enviados al cliente")

# Recibir y enviar mensajes cifrados
while True:
    # Recibir mensaje cifrado y el nonce del cliente
    data = client_socket.recv(1024)
    nonceRecived = client_socket.recv(8)
    if not data:
        break
    # Descifrar el mensaje recibido
    decrypted_message = decrypt_salsa20(key, data,nonceRecived)
    print(f"Cliente salsa 20: {decrypted_message.decode('utf-8')}")
    if decrypted_message.decode('utf-8') == "adios":
        break
    
    # Enviar respuesta cifrada al cliente
    message = input("Servidor salsa 20: ").encode('utf-8')
    nonceSent = os.urandom(8) 

    # Cifrar el mensaje
    encrypted_message = encrypt_salsa20(key, message, nonceSent)

    # Enviar el mensaje cifrado y el nonce al cliente
    client_socket.send(nonceSent)
    client_socket.send(encrypted_message)

# Cerrar la conexión
client_socket.close()
server_socket.close()
