import socket
import sys

HOST = ""

PORT = 9090

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("socket has been created")

try:
    mySocket.bind((HOST, PORT))
except mySocket.Error as msg:
    print