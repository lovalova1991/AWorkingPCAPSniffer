import socket

_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

_socket.connect(("127.0.0.1", 3000))

file = open("image.jpg", "rb")

l = file.read(1024)
while(l):
    print("Sending.. " + str(l))
    _socket.sendall(l)
    l = file.read(1024)