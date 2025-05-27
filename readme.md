# 🔒 Projeto de Criptografia e Descriptografia com AES (Modo CTR)

Este projeto demonstra como **criptografar e descriptografar arquivos** usando o algoritmo **AES (Advanced Encryption Standard)** em **modo CTR**.  
É destinado **exclusivamente para fins educativos** e para aprendizado sobre **segurança da informação**.

---

## 📁 Estrutura do Projeto

- `encrypter.py` – Script para **criptografar** arquivos usando AES.
- `decrypter.py` – Script para **descriptografar** arquivos previamente criptografados.
- `key.bin` – Arquivo onde a chave de criptografia é armazenada para futura recuperação.

---

## 📦 Instalação de Dependências

Antes de rodar os scripts, instale os pacotes necessários com:

```bash
pip install pyaes

🚀 Como Usar
🔐 1️⃣ Criptografar um Arquivo
Execute o comando abaixo para criptografar um arquivo:

BASH: python encrypter.py

✅ O script irá:

Solicitar o nome do arquivo original

Gerar a chave (caso não exista)

Criar um novo arquivo criptografado no formato nome.ext.enc

Salvar a chave no arquivo key.bin

🔓 2️⃣ Descriptografar o Arquivo
Para recuperar o arquivo original:

BASH: python decrypter.py

✅ O script irá:

Ler o conteúdo criptografado

Utilizar a chave salva em key.bin

Gerar o arquivo original descriptografado

 Aviso Importante
Este projeto foi desenvolvido exclusivamente para fins educacionais.
Ele não deve ser utilizado para atividades maliciosas, como ransomware, espionagem ou ataques cibernéticos.
O objetivo é promover o aprendizado seguro sobre criptografia e segurança de dados.