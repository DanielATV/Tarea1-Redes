import socket as skt
direccionServidor = "localhost"
puertoServidor = 61234

socketCliente = skt.socket(skt.AF_INET, skt.SOCK_STREAM)

socketCliente.connect((direccionServidor, puertoServidor))

send = input("Blah: ")

socketCliente.send(send.encode())

respuesta = socketCliente.recv(2048).decode()
print(respuesta)
socketCliente.close()