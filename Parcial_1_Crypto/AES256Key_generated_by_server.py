# AES key in hexadecimal form
key_hex = 'Ejemplo: 131335c96d9e7f83c82228d5540cc8c3ee0242eb9c9d23cb8027a9cc647df7e6'

# Convert the key from hex to bytes
key = bytes.fromhex(key_hex)

# Save the key to a .bin file
with open('aes_key.bin', 'wb') as key_file:
    key_file.write(key)

print("Key has been saved to aes_key.bin")
