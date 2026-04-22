# cliente_eco.py

import socket

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(('127.0.0.1', 12345))  # ou o IP do servidor

mensagem = input("Digite algo para enviar ao servidor: ")
cliente.send(mensagem.encode())

resposta = cliente.recv(1024)
print(f"Servidor respondeu (ECO): {resposta.decode()}")

cliente.close()

