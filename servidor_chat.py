import socket
import threading

# Lista para armazenar todos os clientes conectados
clientes = []

def enviar_para_todos(mensagem, cliente_atual):
    """Envia a mensagem para todos os outros clientes"""
    for cliente in clientes:
        if cliente != cliente_atual:
            try:
                cliente.send(mensagem)
            except:
                # Remove cliente com problema
                clientes.remove(cliente)

def tratar_cliente(cliente, endereco):
    """Recebe mensagens de um cliente e reparte para os outros"""
    print(f"[CONECTADO] {endereco} entrou no chat")
    
    # Envia boas-vindas para o cliente
    cliente.send(b"Bem-vindo ao Chat Interno! Digite 'sair' para encerrar.\n")
    
    while True:
        try:
            mensagem = cliente.recv(1024)
            if not mensagem or mensagem.decode().lower() == 'sair':
                break
            
            print(f"[{endereco}] diz: {mensagem.decode()}")
            # Envia a mensagem para todos os outros clientes
            enviar_para_todos(mensagem, cliente)
            
        except:
            break
    
    # Remove cliente ao desconectar
    clientes.remove(cliente)
    print(f"[DESCONECTADO] {endereco} saiu do chat")
    cliente.close()

# Configuração do servidor
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
porta = 12345

servidor.bind((host, porta))
servidor.listen(5)
print(f"SERVIDOR DO CHAT rodando em {host}:{porta}")
print("Aguardando alunos se conectarem...")

# Aceita conexões infinitamente
while True:
    cliente, endereco = servidor.accept()
    clientes.append(cliente)
    
    # Cria uma thread para cada cliente
    thread = threading.Thread(target=tratar_cliente, args=(cliente, endereco))
    thread.start()