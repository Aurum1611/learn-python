import socket

s=socket.socket()

host='localhost'
port=1957

s.bind((host,port))

s.listen(1)
print("Server",host,':',port,"is listening.")

c,addr=s.accept()
print("Connection established with",str(addr))

fileName=c.recv(1024)

try:
    f=open(fileName,"rb")
    content=f.read()
    c.send(content)
    f.close()
except FileNotFoundError:
    c.send("Requested file not found".encode())

c.close()

