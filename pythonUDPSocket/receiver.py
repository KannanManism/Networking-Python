import socket
import sys
import select

receiver = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
port = 12345
buf = 1024
host = sys.argv[1]
addr = (host,port)
receiver.bind((host,port))

data, addr = receiver.recvfrom(buf)
print(("Received File name: {}").format(data))
f = open("receivedFile","wb")
data, addr = receiver.recvfrom(buf)
try:
    while data:
        f.write(data)
        receiver.settimeout(2)
        data, addr = receiver.recvfrom(buf)
except timeout:
    f.close()
    receiver.close()
    print("File Received")
    
