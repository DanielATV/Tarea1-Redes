import socket as skt
direccionServidor = "localhost"
puertoServidor = 61335

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


#print(ulrHeader.decode())
socketUDP.close()

archivo = open("URL.txt", 'a')
archivo.write(send + '\n')
archivo.write(ulrHeader.decode())
archivo.write("\n\n")
archivo.close()
socketCliente.close()