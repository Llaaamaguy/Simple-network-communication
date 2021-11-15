import socket
from threading import Thread

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('0.tcp.ngrok.io', 18585))
connection = client_socket.makefile('wb')


def receive():
    while True:
        data = client_socket.recv(4096).decode()
        if not data:
            pass
        else:
            print(str(data))


counter = 0
while True:
    client_socket.send("Data".encode('utf-8'))

    counter += 1
    if counter == 1:
        Thread(target=receive).start()
