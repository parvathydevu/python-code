import socket
s=socket.socket() # Create a socket object
s.bind(('127.0.0.1', 1000))# Bind to the port
s.listen(5)   # Now wait for client connection
while True:
    c,addr=s.accept()  # Establish connection with client.
    print ('Got connection from', addr)
    c.send(bytes('Thank you for connecting', 'utf-8'))
    c.close()                # Close the connection
