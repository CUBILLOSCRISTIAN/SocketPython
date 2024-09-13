import socket
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# Configuración del servidor
HOST = '0.0.0.0'
PORT = 5547

# Función para descifrar un mensaje con AES-256 CBC
def decrypt_message(key, iv, ciphertext):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return plaintext

# Crear una llave AES de 256 bits (32 bytes) y almacenarla en un archivo
key = get_random_bytes(32)
with open('aes_key.bin', 'wb') as key_file:
    key_file.write(key)
print(f"Llave AES generada y almacenada en aes_key.bin: {key.hex()}")

# Crear socket del servidor
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    print(f"Servidor escuchando en {HOST}:{PORT}")
    
    conn, addr = server_socket.accept()
    with conn:
        print(f"Conectado por {addr}")
        
        # Recibir el IV y el mensaje cifrado del cliente
        iv = conn.recv(16)  # Recibe el IV de 16 bytes
        ciphertext = conn.recv(1024)  # Recibe el mensaje cifrado
        
        # Descifrar el mensaje
        mensaje_descifrado = decrypt_message(key, iv, ciphertext)
        print(f"Mensaje descifrado: {mensaje_descifrado.decode('utf-8')}")