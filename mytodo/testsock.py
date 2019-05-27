import socket #import the socket module

s = socket.socket() #Create a socket object
host = socket.gethostname() #Get the local machine name
print(host)
# s.close()
port = 12397 # Reserve a port for your service
s.bind((host,port)) #Bind to the port

s.listen(5) #Wait for the client connection
while True:
    c,addr = s.accept() #Establish a connection with the client
    print ("Got connection from {}".format(addr))
    c.send(b"Thank you for connecting!")
    c.close()