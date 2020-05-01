import socket as skt

puertoServidor = 60339
puertoUDP = 60239


socketServidor = skt.socket(skt.AF_INET, skt.SOCK_STREAM)
socketServidor.bind(('', puertoServidor))

socketServidor.listen(1)


socketCliente, direccionCliente = socketServidor.accept()

while True:

    print("Empieza el while")


   
    
    mensaje = socketCliente.recv(2048).decode()
    print("Recivio mensaje")

    if mensaje == "terminate":
        socketCliente.close()
    

    else:

        print("Else")

        socketURL = skt.socket(skt.AF_INET, skt.SOCK_STREAM)

        socketURL.connect((mensaje,80))

        request = "GET / HTTP/1.1\r\nHost: " + mensaje + "\r\n\r\n"


        socketURL.sendall(request.encode())

        data = socketURL.recv(1024)

        respuesta = data.decode()

        n = 0

        for char in respuesta:
            if char == '\r' and respuesta[n+1] == '\n' and respuesta[n+2] == '\r':
                endHeader= n+2
                break
                
                

            n = n+1

        headerUrl = respuesta[:n]

        #mandarPuerto = "OK_"+ str(puertoUDP)

        msg2= str(puertoUDP)


        
        #lista = respuesta.split("\r\n")
        
        #print(lista)


        #Socket UDP
        socketUDP = skt.socket(skt.AF_INET,skt.SOCK_DGRAM)
        socketUDP.bind(('',puertoUDP))

        socketCliente.send(msg2.encode())

        mensajeUDP, asd = socketUDP.recvfrom(2048)
        print(mensajeUDP)

        

        if mensajeUDP.decode() == "OK":
            print("Entre")
            socketUDP.sendto(headerUrl.encode(),asd)
            print("Envie")
            

        socketUDP.close()
        

    


    
