import socket

#socket object creation
clientSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

msg = bytes("hello UDP",'utf-8')
#send message directly to UDP server
clientSocket.sendto(msg,('127.0.0.1',12345))

with open("receivedFile","wb") as file:
    print("File opened")
    while True:
        print("Inside Loop")
        data, addr = clientSocket.recvfrom(1024)
        print(("Data:{}").format(data))
        print(("Received File:{}").format(repr(data)))
        if not data:
            break
        file.write(data)
file.close()
print("Successfully received file")
