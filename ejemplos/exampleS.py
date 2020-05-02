import socket
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind(('',61439 ))
serv.listen(5)
while True:
    conn, addr = serv.accept()
    from_client = ''
    while True:
        data = conn.recv(4096).decode()
        print(len(data))
        if  data == "terminate": 
            break
        from_client = data
        print (from_client)
        msg = "I am SERVER<br>"
        conn.send(msg.encode())
    conn.close()
    print ('client disconnected')