import socket
host = '127.0.0.2'
port =  5555
s = socket.socket()
s.connect((host,port))
s = "hi man its working !"
s.sendall(str.encode(s))
