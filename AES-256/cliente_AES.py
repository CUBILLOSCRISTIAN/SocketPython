import socket
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes

# Configuración del cliente
HOST = '127.0.0.1'
PORT = 8080

# Función para cifrar un mensaje con AES-256 CBC
def encrypt_message(key, message):
    iv = get_random_bytes(16)  # Generar un IV de 16 bytes
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = iv + cipher.encrypt(pad(message.encode('utf-8'), AES.block_size))
    return ciphertext

# Cargar la llave AES desde el archivo
with open('aes_key.bin', 'rb') as key_file:
    key = key_file.read()
print(f"Llave AES cargada: {key.hex()}")

# Crear socket del cliente
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))
    
    # Mensaje a cifrar
    mensaje_cliente = "Hola, servidor. Este es un mensaje cifrado con AES-256-CBC."
    
    # Cifrar el mensaje y enviar
    mensaje_cifrado = encrypt_message(key, mensaje_cliente)
    client_socket.sendall(mensaje_cifrado[:16])  # Enviar el IV
    client_socket.sendall(mensaje_cifrado[16:])  # Enviar el mensaje cifrado