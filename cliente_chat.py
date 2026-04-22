import socket
import threading

def receber_mensagens(cliente):
    """Recebe mensagens do servidor e exibe na tela"""
    while True:
        try:
            mensagem = cliente.recv(1024)
            if mensagem:
                print(f"\n[CHAT] {mensagem.decode()}")
                print("Você: ", end="", flush=True)
        except:
            print("\n[!] Conexão perdida com o servidor")
            cliente.close()
            break

def enviar_mensagens(cliente):
    """Lê o que o usuário digita e envia ao servidor"""
    while True:
        mensagem = input("Você: ")
        if mensagem.lower() == 'sair':
            cliente.send(b'sair')
            cliente.close()
            break
        cliente.send(mensagem.encode())

# Conecta ao servidor
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(('127.0.0.1', 12345))

# Cria threads para receber e enviar mensagens
thread_receber = threading.Thread(target=receber_mensagens, args=(cliente,))
thread_enviar = threading.Thread(target=enviar_mensagens, args=(cliente,))

thread_receber.start()
thread_enviar.start()