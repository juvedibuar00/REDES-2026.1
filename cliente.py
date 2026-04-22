import socket

# Cria o socket TCP
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conecta ao servidor (mesmo computador, porta 12345)
cliente.connect(('127.0.0.1', 12345))

# Recebe a mensagem de boas-vindas
mensagem = cliente.recv(1024)
print(mensagem.decode())

# Lê o que o usuário quer enviar
texto = input("Sua mensagem: ")

# Envia o texto para o servidor
cliente.send(texto.encode())

# Recebe a resposta do servidor
resposta = cliente.recv(1024)
print(f"Servidor respondeu: {resposta.decode()}")

# Fecha a conexão
cliente.close()