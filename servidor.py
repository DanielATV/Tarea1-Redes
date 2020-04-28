import socket as skt

puertoServidor = 61234


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

    while True:

        data = socketURL.recv(1024)

        if data.decode() == "\r\n":
            break

        print(data.decode(),len(data.decode()) )
        
    # hay que leer linea por linea el data
    #respuesta = "queso"
    #socketCliente.send(respuesta.encode())
    socketCliente.close()
