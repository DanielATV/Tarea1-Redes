import socket

direccionServidor = "localhost"
puertoServidor = 61234

socketCliente = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

aMensaje = input("asd")

socketCliente.sendto(aMensaje.encode(),(direccionServidor,puertoServidor))

mensaje,_ = socketCliente.recvfrom(2048)

print(mensaje.decode())

socketCliente.close()