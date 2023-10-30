import socket
import sys
HOST = ""

PORT = 9090

mySocket = socket.socket(socket.AF_INEt, socket.SOCK_STREAM)
print("socket has benn created")

try:
    mySocket.bind((HOST, PORT))
except mySocket.Error as msg:
    print("Binding has failed.Error as Code: + str(msg[0] + 'message' (msg[1]))")