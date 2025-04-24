import socket  # Import socket module

s=socket.socket()  # Create a socket object
s.connect(('127.0.0.1', 1000))
print (s.recv(1024))
s.close()   #close the socket when done 