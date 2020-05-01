import socket

serverPort = 61234

socketServidor = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

socketServidor.bind(('',serverPort))

print(socketServidor.getsockname())

while True:
    mensaje, direccionCliente = socketServidor.recvfrom(2048)
    decodificado = mensaje.decode()
    print(decodificado)

    respuesta = "respuesta" + decodificado.upper()
    socketServidor.sendto(respuesta.encode(),direccionCliente)