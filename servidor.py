import socket, _thread

conexao = []

def connect_cliente(conexao: socket.socket, endereco: str) -> None:
    while True:
        try:
            mensagem = conexao.recv(1024).decode()
            if mensagem:
                print(f' de {endereco[0]} :{endereco[1]} - {mensagem}')
                msg_to_send = f' de {endereco[0]} :{endereco[1]} - {mensagem}'
                listar(msg_to_send, endereco)
            else:
                fechar_conexao(conexao)
                exit(0)
                break
        except Exception:
            print(f'erro a se conectar ao cliente:{endereco[0]} :{endereco[1]}')
            fechar_conexao(conexao)
            break

def listar(msg: str, connection: socket.socket) -> None:
  for cliente_conn in conexao:
    if cliente_conn != conexao:
        cliente_conn.send(msg.encode())


def fechar_conexao(conn: socket.socket) -> None:
    if conn in conexao:
        conexao.remove(conn)

def servidor() -> None:
    LISTENING_PORT = 12000
    socket_instance = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_instance.bind(('', LISTENING_PORT))
    socket_instance.listen(4)
    while True:
        try:
            socket_conexao, endereco = socket_instance.accept()
            conexao.append(socket_conexao)
            _thread.start_new_thread(connect_cliente, (socket_conexao, endereco))
        except KeyboardInterrupt:
            print('Fechado')
            exit(0)
            break


servidor()
