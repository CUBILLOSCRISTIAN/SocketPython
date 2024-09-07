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

# Clave y nonce para Salsa20
key = os.urandom(32)  # Genera una clave secreta de 256 bits (32 bytes)
nonce = os.urandom(8)  # Nonce de 64 bits (8 bytes)

HOST = '0.0.0.0'
PORT = 12345

# Crear el socket TCP/IP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print(f"Servidor escuchando en {HOST}:{PORT}...")

# Esperar una conexión
conn, addr = server_socket.accept()
print(f"Conexión establecida con {addr}")

# Enviar la clave y el nonce al cliente
conn.sendall(key)
conn.sendall(nonce)

while True:
    data = conn.recv(1024)  # Recibir datos cifrados del cliente
    if not data:
        break
    decrypted_message = decrypt_message(key, nonce, data)
    print(f"Cliente: {decrypted_message.decode()}")

    # Enviar respuesta cifrada
    response = "Mensaje recibido por el servidor".encode()
    encrypted_response = encrypt_message(key, nonce, response)
    conn.sendall(encrypted_response)

conn.close()
server_socket.close()
