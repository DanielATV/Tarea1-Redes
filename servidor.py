import socket as skt

puertoServidor = 60339
puertoUDP = 60239


socketServidor = skt.socket(skt.AF_INET, skt.SOCK_STREAM)
socketServidor.bind(('', puertoServidor))

socketServidor.listen(1)



while True:

    print("Esperando clientes")
    socketCliente, direccionCliente = socketServidor.accept()

    while True:

        print("Cliente conectado")
        mensaje = socketCliente.recv(2048).decode()
        

        if mensaje == "terminate":
            socketCliente.close()
            print("Cliente desconectado")
            break

        #Socket TCP para consulta HTTP

        socketURL = skt.socket(skt.AF_INET, skt.SOCK_STREAM)

        socketURL.connect((mensaje,80))

        request = "GET / HTTP/1.1\r\nHost: " + mensaje + "\r\n\r\n"


        socketURL.sendall(request.encode())

        data = socketURL.recv(1024)

        respuesta = data.decode()

        #Rescartar Header

        n = 0

        for char in respuesta:
            if char == '\r' and respuesta[n+1] == '\n' and respuesta[n+2] == '\r':
                endHeader= n+2
                break
                
                

            n = n+1

        headerUrl = respuesta[:n]

        msg2= str(puertoUDP)


        #Socket UDP
        socketUDP = skt.socket(skt.AF_INET,skt.SOCK_DGRAM)
        socketUDP.bind(('',puertoUDP))

        socketCliente.send(msg2.encode())

        mensajeUDP, asd = socketUDP.recvfrom(2048)
        print(mensajeUDP)

        

        if mensajeUDP.decode() == "OK":
            print("Empezando transferencia")
            socketUDP.sendto(headerUrl.encode(),asd)
            print("Termino de transferencia")
            

        socketUDP.close()