import socket

# Cria o socket TCP
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define o endereço e porta
host = '127.0.0.1'  # localhost
porta = 12345

# Liga o socket a este endereço/porta
servidor.bind((host, porta))

# Fica escutando por até 5 conexões
servidor.listen(5)
print(f"Servidor ouvindo em {host}:{porta}...")

# Aceita uma conexão
cliente, endereco = servidor.accept()
print(f"Conexão recebida de {endereco}")

# Envia uma mensagem de boas-vindas
cliente.send(b"Bem-vindo ao servidor! Digite algo:\n")

# Recebe dados do cliente (máximo 1024 bytes)
dados = cliente.recv(1024)
print(f"Cliente disse: {dados.decode()}")

# Envia uma resposta
cliente.send(b"Mensagem recebida com sucesso!")

# Fecha a conexão
cliente.close()
servidor.close()