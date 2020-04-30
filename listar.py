import socket

def listar_cliente() -> None:
  try:
    HOST = 'localhost'
    PORT = 12000
    socket_instance = socket.socket()
    socket_instance.connect((HOST,PORT))
    while True:
          server_msg = socket_instance.recv(1024)
          print(server_msg.decode())

  except KeyboardInterrupt:
    print('fechdo')
    exit(0)
  except Exception :
    print('Erro ao conectar ao servidor')

listar_cliente()
