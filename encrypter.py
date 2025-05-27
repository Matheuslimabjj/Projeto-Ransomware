import os
import pyaes

# Criar uma chave de criptografia forte (16 bytes)
key = os.urandom(16)  

# Nome do arquivo a ser criptografado
file_name = "teste.txt"

# Abrir e ler o arquivo original
with open(file_name, "rb") as file:
    file_data = file.read()

# Remover o arquivo original para evitar exposição
os.remove(file_name)

# Inicializar o AES no modo CTR
aes = pyaes.AESModeOfOperationCTR(key)

# Criptografar os dados
crypto_data = aes.encrypt(file_data)

# Salvar o arquivo criptografado
new_file_name = f"{file_name}.enc"
with open(new_file_name, "wb") as new_file:
    new_file.write(crypto_data)

# Salvar a chave para futura descriptografia (Atenção: Não exponha a chave!)
with open("key.bin", "wb") as key_file:
    key_file.write(key)

print(f"Arquivo criptografado salvo como {new_file_name}")
print("Chave de criptografia armazenada em 'key.bin'")
