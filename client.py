import copy
import socket
from utils import output, loop_int_input
import os

def UDPclient(out_lck, host, port):
    fileList = []
    _socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    _socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    try:
        #_socket.connect(("127.0.0.1", 3000))
        _socket.connect((host, port))

        i = 1
        for file in os.listdir("examplefiles"):
            output(out_lck, "%s %s" % (i, file))
            fileList.append(str(file))
            i += 1

        nfile = loop_int_input(out_lck, "Choose file")
        nf = int(nfile) - 1
        filename = copy.copy(fileList[nf])
        f = open("examplefiles/" + filename, 'rb')
        l = f.read(1024)
        while l:
            output(out_lck, "Sending.. " + str(l))
            _socket.sendall(l)
            l = f.read(1024)
    except socket.error as msg:
        output(out_lck, msg)
        exit(1)
    _socket.close()


def TCPclient(out_lck, host, port):

    _socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    _socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    fileList = []

    try:
        _socket.connect((host, port))
        #_socket.connect(("127.0.0.1", 3000))

        i = 1
        for file in os.listdir("examplefiles"):
            output(out_lck, "%s %s" % (i, file))
            fileList.append(str(file))
            i += 1

        nfile = loop_int_input(out_lck, "Choose file")
        nf = int(nfile) - 1
        filename = copy.copy(fileList[nf])
        f = open("examplefiles/" + filename, 'rb')
        l = f.read(1024)
        while l:
            _socket.send(l)
            l = f.read(1024)
        f.close()
    except socket.error as msg:
        output(out_lck, msg)
        exit(2)
    _socket.close()