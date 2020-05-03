import socket as skt

#funciones para el cache

def leer_Cache():
    try:
        arch = open("cache.txt","r")
        l=[]
        a = ""
        name = ""
        for i in arch:

            comparar = i.strip()
            
         
            if(a == "" and name== ""):
                name = i
                name=name.strip()
                continue
            if(comparar == "----------"):
                print("entre")
                l.append((name,a))
                a = ""
                name=""
                continue
            a += i
        arch.close()
        return l

    except:
        arch = open("cache.txt","w")
        arch.close()
        l = []
        return l

def escribir_cache(l):
    arch = open("cache.txt","w")
    for url,header in l:
        arch.write(url+'\n')
        arch.write(header)
        arch.write("\n----------\n")
    arch.close()

def limites(l):
    if(len(l)>5):
        return l[len(l)-5:]
    else:
        return l

cache = leer_Cache()

puertoServidor = 60331
puertoUDP = 61231


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
        
        flag = 0
        for nombre,encabezado in cache:
            if mensaje == nombre:
                headerUrl = encabezado
                flag = 1

            
        if flag == 0:

            #Consulta HTTP

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

            cache.append((mensaje,headerUrl))
            cache = limites(cache)
            escribir_cache(cache)

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