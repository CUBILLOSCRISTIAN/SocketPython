import socket
from Crypto.Cipher import Salsa20
import os

def encrypt_salsa20(key, plaintext, nonce):
    cipher = Salsa20.new(key=key, nonce=nonce)
    ciphertext = cipher.encrypt(plaintext)
    return ciphertext

def decrypt_salsa20(key, ciphertext, nonce):
    cipher = Salsa20.new(key=key, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext

# Crear el socket del cliente
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_ip = '192.168.43.149' # IP del servidor
server_port = 8080       # Puerto del servidor

# Conectarse al servidor
client_socket.connect((server_ip, server_port))
print(f"Conectado al servidor en {server_ip}:{server_port}")

# Recibir clave y nonce del servidor
key = client_socket.recv(32)


print("Llave simétrica y nonce recibidos")

while True:
    message = input("Cliente salsa 20: ").encode('utf-8')
    
    nonceSent = os.urandom(8)
    encrypted_message = encrypt_salsa20(key, message, nonceSent) # Cifrar el mensaje
    
    # Enviar el mensaje cifrado y el nonce al servidor
    client_socket.send(nonceSent)
    client_socket.send(encrypted_message)

    # Recibir mensaje cifrado y el nonce del servidor
    data = client_socket.recv(1024)
    nonceReceived = client_socket.recv(8)
    if not data:
        break

    decrypted_message = decrypt_salsa20(key, data,nonceReceived) # Descifrar el mensaje
    print(f"Servidor salsa 20: {decrypted_message.decode('utf-8')}")
    
# Cerrar la conexión
client_socket.close()