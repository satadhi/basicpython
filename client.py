import socket
host = '127.0.0.2'
port =  5555
s = socket.socket()
s.bind((host,port))
s.sendall("hi man its working !".encode())
