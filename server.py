import socket
from utils import output


def UDPserver(out_lck, host, port, extension):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    f = open('output/UDPreceived.' + extension, 'wb')
    try:
        sock.bind((host, port))

        output(out_lck, "Listening....\n")
        data, address = sock.recvfrom(1024)
        while len(data) > 0:
            data, address = sock.recvfrom(1024)
            f.write(data)
            print("Received: " + str(data))
    except socket.error as msg:
        output(out_lck, msg)
        exit(3)
    sock.close()


def TCPserver(out_lck, host, port, extension):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    try:
        output(out_lck, "Listening....\n")
        s.bind((host, port))  # inizializzazione della connessione
        s.listen(100)
        conn, addr = s.accept()
        f = open('output/TCPreceived.' + extension, 'wb')
        size = 1024
        data = conn.recv(size)

        while len(data) > 0:
            f.write(data)
            data = conn.recv(size)
        f.close()
    except socket.error as msg:
        output(out_lck, msg)
        exit(4)
    s.close()