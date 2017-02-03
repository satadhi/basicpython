import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server = 'pythonprogramming.net'
def pscan(port):
    try:
        s.connect((server,port))
        return True
    except:
        return False
for x in range(100):
    if pscan(x):
        print("port no :",x,"is open")
    else:
        print("port no :",x,"is closed")
