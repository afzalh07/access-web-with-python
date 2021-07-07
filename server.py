import socket

# create the server socket; AF_INET = ipv4; SOCK_STREAM = TCP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# binding the server socket to the 1234 port of the server
host = socket.gethostname()
server.bind((host, 1234))

# making a queue of 5 for incoming connection
server.listen(5)

while True:
    # this acknowledges the other endpoint (socket of the client)
    c, addr = server.accept()
    print("Got connection from", addr)

    # sends data to the client
    c.send(bytes('thank you for connecting', "utf-8"))

    # closeing the socket
    c.close()
