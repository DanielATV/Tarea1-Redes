import socket as skt
direccionServidor = "localhost"
puertoServidor = 61235

socketCliente = skt.socket(skt.AF_INET, skt.SOCK_STREAM)

socketCliente.connect((direccionServidor, puertoServidor))

send = "webcode.me"



socketCliente.send(send.encode())

respuesta = socketCliente.recv(2048).decode()
print(respuesta)
socketCliente.close()