import socket
from Crypto.Cipher import Salsa20
import os

def encrypt_salsa20(key, plaintext, nonce):
    cipher = Salsa20.new(key=key, nonce=nonce)
    ciphertext = cipher.encrypt(plaintext)
    return nonce + ciphertext  # Enviar el nonce junto con el mensaje cifrado

def decrypt_salsa20(key, nonce_and_ciphertext):
    nonce = nonce_and_ciphertext[:8]  # Extraer el nonce
    ciphertext = nonce_and_ciphertext[8:]  # Extraer el mensaje cifrado
    cipher = Salsa20.new(key=key, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext

# Crear el socket del cliente
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_ip = '192.168.43.149'  # IP del servidor
server_port = 8080  # Puerto del servidor

# Conectarse al servidor
client_socket.connect((server_ip, server_port))
print(f"Conectado al servidor en {server_ip}:{server_port}")

# Recibir clave del servidor
key = client_socket.recv(32)
print("Llave simétrica recibida")

while True:
    # Enviar mensaje cifrado al servidor
    message = input("Cliente salsa 20: ").encode('utf-8')
    nonce = os.urandom(8)  # Generar un nuevo nonce para cada mensaje
    encrypted_message = encrypt_salsa20(key, message, nonce)
    client_socket.sendall(encrypted_message)

    # Recibir mensaje cifrado del servidor
    nonce_and_ciphertext = client_socket.recv(1024)
    if not nonce_and_ciphertext:
        break
    decrypted_message = decrypt_salsa20(key, nonce_and_ciphertext)
    print(f"Servidor salsa 20: {decrypted_message.decode('utf-8')}")
    if decrypted_message.decode('utf-8') == "adios":
        break

# Cerrar la conexión
client_socket.close()