import socket as skt

puertoServidor = 61235


socketServidor = skt.socket(skt.AF_INET, skt.SOCK_STREAM)
socketServidor.bind(('', puertoServidor))

socketServidor.listen(1)

while True:

    socketCliente, direccionCliente = socketServidor.accept()
    mensaje = socketCliente.recv(2048).decode()




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

    print(respuesta[:n])
    #lista = respuesta.split("\r\n")
    
    #print(lista)
    # hay que leer linea por linea el data
    #respuesta = "queso"
    #socketCliente.send(respuesta.encode())
    socketCliente.close()
