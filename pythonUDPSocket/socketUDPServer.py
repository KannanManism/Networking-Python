import socket

#socket creation
serverSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#binds connection
serverSocket.bind(('127.0.0.1',12345))

#file reading
file = open("demofile.txt","r")
l = file.read(1024)
print(("File: {} ").format(l))
byt = bytes(l,"utf-8")


while True:    
#data, addr = serverSocket.recvfrom(1024)
#print(('message from {}').format(addr))
#print(('Message is: {}').format(data))
    while(l):
        serverSocket.sendto(byt,('127.0.0.1',12345))
        l = file.read(1024)
        byt = bytes(l,"utf-8")
    file.close()
    print("Done sending file")
    print("[-] Waiting for next connection")
    thankYouMsg = "Thank you for connecting"
    th = bytes(thankYouMsg,"utf-8")
    serverSocket.sendto(th,('127.0.0.1',12345))
    
        
