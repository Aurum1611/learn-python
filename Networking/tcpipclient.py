import socket

s=socket.socket()

try:
    s.connect(("localhost",8000))
    
    msg=s.recv(1024)
    while msg:
        print('Received:',msg.decode())
        msg=s.recv(1024)
    
except:
    print("Server connection couldn't be established")

s.close()
