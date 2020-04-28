import socket as skt

puertoServidor = 61234

socketServidor = skt.socket(skt.AF_INET, skt.SOCK_STREAM)
socketServidor.bind(('', puertoServidor))

socketServidor.listen(1)

while True:

    socketCliente, direccionCliente = socketServidor.accept()
    mensaje = socketCliente.recv(2048).decode()

    respuesta = "queso"
    socketCliente.send(respuesta.encode())
    socketCliente.close()
