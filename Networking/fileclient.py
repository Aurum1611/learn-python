import socket

s=socket.socket()

try:
    s.connect(('localhost',1957))
    
    filename= input("Enter a filename along with it's extension:") # lorem_ipsum.txt is one file already present
    s.send(filename.encode())
    
    msg=s.recv(1024)
    while msg:
        print(msg.decode())
        msg=s.recv(1024)
    
except:
    print("Server connection couldn't be established")

s.close()