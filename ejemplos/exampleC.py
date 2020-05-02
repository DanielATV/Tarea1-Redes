import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 61439))
while True:
    msg = input("asd: ")
    if msg == "terminate":
        client.send(msg.encode())
        break
    else:

        client.send(msg.encode())
        from_server = client.recv(4096).decode()
client.close()
print (from_server)