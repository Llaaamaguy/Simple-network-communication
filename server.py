import socket

HOST = ''
PORT = 8485

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print('Socket created')

s.bind((HOST,PORT))
print('Socket bind complete')
s.listen(10)
print('Socket now listening')

conn,addr=s.accept()

while True:
    data = conn.recv(4096).decode()
    if not data:
        pass
    else:
        print(str(data))

    conn.send("Got packet {}".format(data).encode('utf-8'))
