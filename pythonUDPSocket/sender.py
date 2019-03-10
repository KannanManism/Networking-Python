import socket
import sys

sender = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
host = sys.argv[1]
port = 12345
buf = 1024

addr = (host,port)
fileName = sys.argv[2]
print(("{}").format(fileName))
fileNameb=bytes(fileName,'utf-8')
sender.sendto(fileNameb,addr)

f = open(fileName,"rb")
data = f.read(buf)
print(("Data:{}").format(data)) 
#byt = bytes(data,"utf-8")
while data:
    if(sender.sendto(data,addr)):
        print("Sending")
        data = f.read(buf)
        #byt = byte(data,"utf-8")
    else:
        print("Finished Sending")
