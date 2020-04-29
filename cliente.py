import socket

def cliente() -> None:
  try:
    HOST = 'localhost'
    PORT = 12000
    socket_instance = socket.socket()
    socket_instance.connect((HOST, PORT))
    while True:
      try:
        mensagem = input('Digite sua mensagem: ')
        socket_instance.send(mensagem.encode())
      except KeyboardInterrupt:
        print('fechado')
        break
    socket_instance.close()
  except Exception :
    print('Erro ao conectar ao servidor')

cliente()
