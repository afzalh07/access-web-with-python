import socket

# create the client socket; AF_INET = ipv4; SOCK_STREAM = TCP
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connecting the client socket to the port of server
host = socket.gethostname()
client.connect((host, 1234))

# receive data sent by the server
# 1024 is the buffer size at a time
# encoded byte message received
msg = client.recv(1024)
print(msg)

# decode the message from byte to unicode
dec = msg.decode()
print(dec)

# close the socket
client.close()
