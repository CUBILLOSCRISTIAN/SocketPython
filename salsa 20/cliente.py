import socket
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

# Funciones para encriptar y desencriptar con Salsa20
def encrypt_message(key, nonce, message):
    cipher = Cipher(algorithms.Salsa20(key, nonce), mode=None, backend=default_backend())
    encryptor = cipher.encryptor()
    return encryptor.update(message)

def decrypt_message(key, nonce, ciphertext):
    cipher = Cipher(algorithms.Salsa20(key, nonce), mode=None, backend=default_backend())
    decryptor = cipher.decryptor()
    return decryptor.update(ciphertext)

SERVER_HOST = '192.168.18.102'  # Cambia esta IP a la del servidor
SERVER_PORT = 12345

# Crear el socket TCP/IP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectarse al servidor
client_socket.connect((SERVER_HOST, SERVER_PORT))
print(f"Conectado al servidor {SERVER_HOST}:{SERVER_PORT}")

# Recibir clave y nonce del servidor
key = client_socket.recv(32)
nonce = client_socket.recv(8)

while True:
    message = input("Tú: ").encode()
    
    # Encriptar el mensaje antes de enviarlo
    encrypted_message = encrypt_message(key, nonce, message)
    client_socket.sendall(encrypted_message)
    
    # Recibir y desencriptar la respuesta del servidor
    encrypted_response = client_socket.recv(1024)
    decrypted_response = decrypt_message(key, nonce, encrypted_response)
    print(f"Servidor: {decrypted_response.decode()}")

client_socket.close()
