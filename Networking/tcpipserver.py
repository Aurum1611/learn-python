import socket

host="localhost"
port=8000

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind((host,port))

s.listen(1)
print("Server",host,':',port,"is listening.")

c,addr=s.accept()
print("Connection established with",str(addr))

c.send(b"Life's good!")
c.send("I prefer game videos over playing games".encode())

c.close()