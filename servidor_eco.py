
import socket

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind(('0.0.0.0', 12345))  # '0.0.0.0' aceita conexões de qualquer computador
servidor.listen(1)

print("Servidor Eco aguardando conexão...")

cliente, endereco = servidor.accept()
print(f"Cliente conectado de {endereco}")

# Recebe mensagem do cliente
dados = cliente.recv(1024)
print(f"Recebido: {dados.decode()}")

# Envia a MESMA mensagem de volta (ECO)
cliente.send(dados)

cliente.close()
servidor.close()



