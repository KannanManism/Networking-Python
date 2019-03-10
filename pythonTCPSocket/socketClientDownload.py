import socket

#creation of socket object
s = socket.socket()

# assign port
port = 12345

# connect to the serverSocket
s.connect(('127.0.0.1',port))
s.send(b"Hello Server")

with open('received_file','wb') as f:
    print("File opened")
    while True:
        print("receiving file....")
        data = s.recv(1024)
        print(("data {}").format(data))
        if not data:
            break
        f.write(data)
f.close()
print("Successfully received file")

#receive message from server
#receivedMessage = s.recv(1024)

#print(("Message from Server: {}").format(receivedMessage))

s.close()
