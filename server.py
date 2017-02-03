import socket
host = '127.0.0.2'
port =  5555
s = socket.socket()
s.bind((host,port))
s.listen(1)
conn,rport=s.accept()
print("connection from :",rport)
while True:
    data = conn.recv(1024)
    if not data:
        print(data.decode('utf-8'))
        break
