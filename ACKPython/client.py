import socket
import time

def client():
    #creation of socket object
    s = socket.socket()

    # assign port
    port = 12345

    # connect to the serverSocket
    s.connect(('127.0.0.1',port))

    # File size is 1200 Bytes
    # Each packet size is 120 Bytes

    # First File packet
    sequenceNumber = 120

    #receive message from server
    for i in range(0,10):
        sequenceString = str(sequenceNumber)
        sequenceBytes=bytes(sequenceString,"utf-8")
        print(("Sequence Number: {}").format(sequenceString))
        s.send(sequenceBytes)
        time.sleep(1)
        receivedMessage = s.recv(1024)
        ackNumber = int(receivedMessage)
        bufferAck = ackNumber
        
        if sequenceNumber == ackNumber - 1:
            print(("Ack Number: {}").format(ackNumber))
            print(("Message from Server: {}").format(receivedMessage))
        else:
            print(("Ack Number: {}").format(ackNumber))
            print("Wrong ACK !!")
        sequenceNumber=sequenceNumber + 120
    
    s.close()

def main():
    client()

main()



