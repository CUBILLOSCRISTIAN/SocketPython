import socket
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# Configuración del cliente
HOST = '192.168.1.4'
PORT = 8080

# Función para cifrar un mensaje con AES-256 CBC
def encrypt_message(key, message):
    iv = get_random_bytes(16)  # Generar un IV de 16 bytes
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = iv + cipher.encrypt(pad(message.encode('utf-8'), AES.block_size))
    return ciphertext

# Función para descifrar un mensaje con AES-256 CBC
def decrypt_message(key, iv, ciphertext):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return plaintext

# Cargar la llave AES desde el archivo
with open('aes_key.bin', 'rb') as key_file:
    key = key_file.read()
print(f"Llave AES cargada: {key.hex()}")

# Crear socket del cliente
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))
    
    while True:
        # Enviar mensaje
        mensaje_cliente = input("Cliente (tú): ")
        mensaje_cifrado = encrypt_message(key, mensaje_cliente)
        client_socket.sendall(mensaje_cifrado[:16])  # Enviar el IV
        client_socket.sendall(mensaje_cifrado[16:])  # Enviar el mensaje cifrado
        
        # Recibir respuesta del servidor
        iv = client_socket.recv(16)  # Recibe el IV de 16 bytes
        ciphertext = client_socket.recv(1024)  # Recibe el mensaje cifrado
        mensaje_descifrado = decrypt_message(key, iv, ciphertext)
        print(f"Servidor: {mensaje_descifrado.decode('utf-8')}")
