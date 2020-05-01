import socket as skt
direccionServidor = "localhost"
puertoServidor = 61334

socketCliente = skt.socket(skt.AF_INET, skt.SOCK_STREAM)

socketCliente.connect((direccionServidor, puertoServidor))

send = "webcode.me"



socketCliente.send(send.encode())

puertoUDP = socketCliente.recv(2048).decode()
puertoUDP = int(puertoUDP)
print(puertoUDP)



socketUDP = skt.socket(skt.AF_INET,skt.SOCK_DGRAM)

estado= "OK"
print(estado)

socketUDP.sendto(estado.encode(),(direccionServidor,puertoUDP))
print("Envie estado")

ulrHeader,_ = socketUDP.recvfrom(2048)


print(ulrHeader.decode())
socketUDP.close()
socketCliente.close()