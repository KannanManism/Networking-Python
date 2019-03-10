import socket

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

msg = bytes("Hello","utf-8")

while True:
    #accept the incoming connections
    conn, addr = s.accept()
    print(("[+] Connection from {}").format(addr))

    #send back something to clients
    conn.send(b'Thank you for connecting \n')
    #s.sendto(msg,('127.0.0.1',12345))
    conn.close()
