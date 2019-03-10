import socket
import time

def server():
    #creation of socket
    s = socket.socket() # AF_INET,SOCK_STREAM are default
    print("Socket is created")

    #set the port for the server
    port = 12345


    #binds the incoming connection
    s.bind(('127.0.0.1',port))
       
    # Start listening to incoming connections
    s.listen(5) # incoming connections waits if conn > 5
    print("Listening for connections")

    #msg = bytes("Hello","utf-8")

    while True:
        #accept the incoming connections
        conn, addr = s.accept()
        print(("[+] Connection from {}").format(addr))
        for i in range(0,10):
            msg = conn.recv(1024)
            print(("Sequence Number: {} ").format(msg))
            time.sleep(1)
            sequenceNumber = int(msg)
            ackNumber = sequenceNumber + 1
            ackNumber = str(ackNumber)
            ackBytes = bytes(ackNumber,"utf-8")

            #send back something to clients
            conn.send(ackBytes)

def main():
    server()

main()
        
    
