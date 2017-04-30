import socket
port = 3000
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

sock.bind(("", port))

print("Listening....\n")
while True:
    data, address = sock.recvfrom(1024)
    print("Received: " + str(data))