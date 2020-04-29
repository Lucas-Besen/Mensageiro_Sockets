import socket, _thread

conexao = []


def connect_cliente(conexao: socket.socket, endereco: str) -> None:
    while True:
        try:
            mensagem = conexao.recv(1024).decode()
            if mensagem:
                print(f'{endereco[0]}: {endereco[1]} - {mensagem}')
            else:
                fechar_conexao(conexao)
                break
        except Exception:
            print('erro a se conectar ao cliente:')
            fechar_conexao(conexao)
            break


def fechar_conexao(conn: socket.socket) -> None:
    if conn in conexao:
        conexao.remove(conn)


def servidor() -> None:
    LISTENING_PORT = 12000
    try:
        socket_instance = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_instance.bind(('', LISTENING_PORT))
        socket_instance.listen(4)
        while True:
            try:
                socket_conexao, endereco = socket_instance.accept()
                conexao.append(socket_conexao)
                _thread.start_new_thread(connect_cliente, (socket_conexao, endereco))
            except KeyboardInterrupt:
                print("Fechado")
                break
    except Exception:
        print('erro')

servidor()
