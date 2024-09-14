import socket
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# Configuración del servidor
HOST = '0.0.0.0'
PORT = 8080

# Función para descifrar un mensaje con AES-256 CBC
def decrypt_message(key, iv, ciphertext):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return plaintext

# Función para cifrar un mensaje con AES-256 CBC
def encrypt_message(key, message):
    iv = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = iv + cipher.encrypt(pad(message.encode('utf-8'), AES.block_size))
    return ciphertext

# Cargar la llave AES desde el archivo
with open('aes_key.bin', 'rb') as key_file:
    key = key_file.read()
print(f"Llave AES cargada: {key.hex()}")

# Crear socket del servidor
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    print(f"Servidor escuchando en {HOST}:{PORT}")
    
    conn, addr = server_socket.accept()
    with conn:
        print(f"Conectado por {addr}")
        
        while True:
            # Recibir el IV y el mensaje cifrado del cliente
            iv = conn.recv(16)  # Recibe el IV de 16 bytes
            ciphertext = conn.recv(1024)  # Recibe el mensaje cifrado
            
            # Descifrar el mensaje
            mensaje_descifrado = decrypt_message(key, iv, ciphertext)
            print(f"Cliente: {mensaje_descifrado.decode('utf-8')}")
            
            # Enviar respuesta
            respuesta_servidor = input("Servidor (tú): ")
            mensaje_cifrado = encrypt_message(key, respuesta_servidor)
            conn.sendall(mensaje_cifrado[:16])  # Enviar el IV
            conn.sendall(mensaje_cifrado[16:])  # Enviar el mensaje cifrado
