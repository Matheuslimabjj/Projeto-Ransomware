import os
import pyaes

# Nome do arquivo criptografado
file_name = "teste.txt.enc"

# Abrir e ler o arquivo criptografado
with open(file_name, "rb") as file:
    file_data = file.read()

# Recuperar a chave de criptografia salva anteriormente
with open("key.bin", "rb") as key_file:
    key = key_file.read()

# Inicializar o AES no modo CTR
aes = pyaes.AESModeOfOperationCTR(key)

# Descriptografar os dados
decrypt_data = aes.decrypt(file_data)

# Remover o arquivo criptografado após verificar que foi lido corretamente
if file_data:
    os.remove(file_name)

# Criar o arquivo descriptografado
new_file_name = "teste.txt"
with open(new_file_name, "wb") as new_file:
    new_file.write(decrypt_data)

print(f"Arquivo descriptografado salvo como {new_file_name}")
