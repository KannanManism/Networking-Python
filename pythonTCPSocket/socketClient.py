import socket

#creation of socket object
s = socket.socket()

# assign port
port = 12345

# connect to the serverSocket
s.connect(('127.0.0.1',port))

#receive message from server
receivedMessage = s.recv(1024)
print(("Message from Server: {}").format(receivedMessage))

s.close()
